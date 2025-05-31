"""
QA and Report Improvement System
Provides automated quality assessment and iterative report improvement
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from .llm_utils import _call_llm_api


class ReportQASystem:
    """Quality assessment and improvement system for generated reports"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {
            "enabled": True,
            "mode": "auto",  # auto | suggest_only | review_later
            "max_sections": 5,
            "confidence_threshold": 0.7,
            "layers": ["structure", "clarity", "accuracy", "tone"]
        }
    
    def run_report_qa(self, report_content: str, sources: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
        """
        Run comprehensive QA on a generated report
        """
        if not self.config.get("enabled", True):
            return {"status": "disabled", "issues": []}
        
        qa_results = {
            "overall_score": 0.0,
            "layer_scores": {},
            "inaccurate_or_confusing_sections": [],
            "improvement_suggestions": [],
            "confidence": 0.0,
            "auto_fix_recommended": False
        }
        
        # Run layered QA based on configuration
        layers = self.config.get("layers", ["structure", "clarity", "accuracy"])
        
        for layer in layers:
            layer_result = self._run_layer_qa(report_content, sources, query, layer)
            qa_results["layer_scores"][layer] = layer_result
            
            # Aggregate problematic sections
            if "problematic_sections" in layer_result:
                qa_results["inaccurate_or_confusing_sections"].extend(
                    layer_result["problematic_sections"]
                )
        
        # Calculate overall scores
        qa_results["overall_score"] = self._calculate_overall_score(qa_results["layer_scores"])
        qa_results["confidence"] = self._calculate_confidence(qa_results["layer_scores"])
        
        # Use the new trust scoring system for auto-fix recommendations
        fix_decision = self.should_auto_apply_fixes(qa_results)
        qa_results["auto_fix_recommended"] = fix_decision["auto_apply"]
        qa_results["suggest_review"] = fix_decision["suggest_review"]
        qa_results["manual_review_required"] = fix_decision["manual_review_required"]
        qa_results["fix_decision_reasoning"] = fix_decision["reasoning"]
        qa_results["trust_score"] = fix_decision["trust_score"]
        
        return qa_results
    
    def run_layered_qa(self, report_content: str, sources: List[Dict[str, Any]], 
                      query: str, layer_sequence: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Run QA in sequential layers, potentially improving after each layer
        """
        if layer_sequence is None:
            layer_sequence = ["structure", "accuracy", "clarity", "tone"]
        
        current_content = report_content
        layer_results = {}
        overall_improvements = []
        
        for layer in layer_sequence:
            # Run QA for this specific layer
            layer_result = self._run_layer_qa(current_content, sources, query, layer)
            layer_results[layer] = layer_result
            
            # If there are significant issues in this layer, try to fix them
            if (layer_result.get('score', 1.0) < 0.8 and 
                layer_result.get('problematic_sections') and
                len(layer_result['problematic_sections']) <= 3):
                
                try:
                    # Create improvement pipeline for this layer
                    temp_qa = ReportQASystem({
                        "enabled": True,
                        "mode": "auto",
                        "max_sections": 3,
                        "confidence_threshold": 0.7,
                        "layers": [layer]  # Focus on single layer
                    })
                    temp_pipeline = ReportImprovementPipeline(temp_qa)
                    
                    # Apply layer-specific improvements
                    improved_content, improvements = temp_pipeline._apply_fixes(
                        current_content,
                        layer_result['problematic_sections'],
                        sources,
                        query
                    )
                    
                    if improved_content != current_content:
                        current_content = improved_content
                        overall_improvements.extend(improvements)
                        # Re-run QA for this layer to update score
                        layer_results[layer] = self._run_layer_qa(current_content, sources, query, layer)
                        
                except Exception as e:
                    print(f"Error in layered improvement for {layer}: {e}")
        
        # Calculate final overall scores
        overall_score = self._calculate_overall_score(layer_results)
        confidence = self._calculate_confidence(layer_results)
        
        return {
            "overall_score": overall_score,
            "confidence": confidence,
            "layer_results": layer_results,
            "layered_improvements": overall_improvements,
            "improved_content": current_content,
            "layers_processed": layer_sequence,
            "content_changed": current_content != report_content
        }
    
    def _run_layer_qa(self, report_content: str, sources: List[Dict[str, Any]], query: str, layer: str) -> Dict[str, Any]:
        """Run QA for a specific layer (structure, clarity, accuracy, tone)"""
        
        if layer == "structure":
            return self._qa_structure(report_content, query)
        elif layer == "clarity":
            return self._qa_clarity(report_content, query)
        elif layer == "accuracy":
            return self._qa_accuracy(report_content, sources, query)
        elif layer == "tone":
            return self._qa_tone(report_content, query)
        else:
            return {"score": 1.0, "issues": [], "problematic_sections": []}
    
    def _qa_structure(self, report_content: str, query: str) -> Dict[str, Any]:
        """QA for report structure and organization"""
        prompt = f"""Evaluate the structure and organization of this report:

Query: {query}

Report:
{report_content}

Assess:
1. Does the report have a logical flow?
2. Are sections well-organized and appropriately titled?
3. Is there a clear introduction/summary and conclusion?
4. Are there any missing structural elements?

Respond in JSON format:
{{
    "score": 0.0-1.0,
    "issues": ["list of structural issues"],
    "problematic_sections": [
        {{
            "section_title": "section name",
            "issue": "description of issue",
            "suggested_fix": "how to improve"
        }}
    ],
    "strengths": ["list of structural strengths"]
}}"""
        
        return self._parse_qa_response(prompt, "structure QA")
    
    def _qa_clarity(self, report_content: str, query: str) -> Dict[str, Any]:
        """QA for clarity and readability"""
        prompt = f"""Evaluate the clarity and readability of this report:

Query: {query}

Report:
{report_content}

Assess:
1. Is the language clear and accessible?
2. Are technical terms properly explained?
3. Are there any confusing or ambiguous sections?
4. Is the writing concise and well-organized?

Respond in JSON format:
{{
    "score": 0.0-1.0,
    "issues": ["list of clarity issues"],
    "problematic_sections": [
        {{
            "section_title": "section name",
            "issue": "description of clarity issue",
            "suggested_fix": "how to improve clarity"
        }}
    ],
    "strengths": ["list of clarity strengths"]
}}"""
        
        return self._parse_qa_response(prompt, "clarity QA")
    
    def _qa_accuracy(self, report_content: str, sources: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
        """QA for accuracy and source alignment"""
        # Prepare source context
        source_context = ""
        for i, source in enumerate(sources[:5]):
            source_context += f"Source {i+1}: {source.get('title', 'Untitled')}\n"
            source_context += f"{source.get('content', {}).get('body', '')[:500]}...\n\n"
        
        prompt = f"""Evaluate the accuracy of this report against the provided sources:

Query: {query}

Report:
{report_content}

Available Sources:
{source_context}

Assess:
1. Are all claims in the report supported by the sources?
2. Are there any factual inaccuracies or misinterpretations?
3. Are citations used appropriately?
4. Is any important information from sources missing?

Respond in JSON format:
{{
    "score": 0.0-1.0,
    "issues": ["list of accuracy issues"],
    "problematic_sections": [
        {{
            "section_title": "section name",
            "issue": "description of accuracy issue",
            "suggested_fix": "how to improve accuracy",
            "affected_citations": ["[1]", "[2]"]
        }}
    ],
    "strengths": ["list of accuracy strengths"]
}}"""
        
        return self._parse_qa_response(prompt, "accuracy QA")
    
    def _qa_tone(self, report_content: str, query: str) -> Dict[str, Any]:
        """QA for tone and style consistency"""
        prompt = f"""Evaluate the tone and style consistency of this report:

Query: {query}

Report:
{report_content}

Assess:
1. Is the tone appropriate for the subject matter?
2. Is the style consistent throughout?
3. Is the level of formality appropriate?
4. Are there any awkward transitions or inconsistencies?

Respond in JSON format:
{{
    "score": 0.0-1.0,
    "issues": ["list of tone/style issues"],
    "problematic_sections": [
        {{
            "section_title": "section name",
            "issue": "description of tone issue",
            "suggested_fix": "how to improve tone"
        }}
    ],
    "strengths": ["list of tone strengths"]
}}"""
        
        return self._parse_qa_response(prompt, "tone QA")
    
    def _parse_qa_response(self, prompt: str, qa_type: str) -> Dict[str, Any]:
        """Parse QA response from LLM"""
        try:
            response = _call_llm_api(prompt, qa_type)
            if response:
                # Clean JSON response
                if '```json' in response:
                    response = response.split('```json')[1].split('```')[0]
                elif '```' in response:
                    response = response.split('```')[1].split('```')[0]
                
                return json.loads(response.strip())
        except Exception as e:
            print(f"Error in {qa_type}: {e}")
        
        # Fallback
        return {
            "score": 0.8,
            "issues": [],
            "problematic_sections": [],
            "strengths": []
        }
    
    def _calculate_overall_score(self, layer_scores: Dict[str, Dict[str, Any]]) -> float:
        """Calculate overall QA score from layer scores"""
        if not layer_scores:
            return 0.0
        
        # Weight different layers
        weights = {
            "accuracy": 0.4,
            "clarity": 0.3,
            "structure": 0.2,
            "tone": 0.1
        }
        
        total_score = 0.0
        total_weight = 0.0
        
        for layer, result in layer_scores.items():
            weight = weights.get(layer, 0.1)
            score = result.get("score", 0.0)
            total_score += score * weight
            total_weight += weight
        
        return total_score / total_weight if total_weight > 0 else 0.0
    
    def _calculate_confidence(self, layer_scores: Dict[str, Dict[str, Any]]) -> float:
        """Calculate confidence in QA assessment with enhanced trust scoring"""
        if not layer_scores:
            return 0.0
        
        # Confidence based on consistency of scores and number of issues
        scores = [result.get("score", 0.0) for result in layer_scores.values()]
        avg_score = sum(scores) / len(scores)
        
        # Penalize high variance in scores (inconsistency)
        variance = sum((s - avg_score) ** 2 for s in scores) / len(scores)
        consistency_factor = max(0.0, 1.0 - variance * 2)
        
        # Factor in number of issues
        total_issues = sum(len(result.get("issues", [])) for result in layer_scores.values())
        issue_factor = max(0.3, 1.0 - total_issues * 0.1)
        
        # Calculate enhanced trust score
        trust_score = self._calculate_trust_score(layer_scores)
        
        # Combine confidence factors with trust score
        base_confidence = avg_score * consistency_factor * issue_factor
        enhanced_confidence = base_confidence * trust_score
        
        return min(1.0, enhanced_confidence)
    
    def _calculate_trust_score(self, layer_scores: Dict[str, Dict[str, Any]]) -> float:
        """
        Calculate trust score for QA suggestions to determine auto-fix viability
        Returns a multiplier between 0.5 and 1.0
        """
        trust_factors = []
        
        # 1. Source reliability scoring (based on layer consistency)
        accuracy_scores = []
        for layer, result in layer_scores.items():
            if layer == "accuracy":
                accuracy_scores.append(result.get("score", 0.0))
        
        if accuracy_scores:
            source_reliability = sum(accuracy_scores) / len(accuracy_scores)
        else:
            source_reliability = 0.8  # Default if no accuracy layer
        
        trust_factors.append(("source_reliability", source_reliability, 0.4))
        
        # 2. Fix complexity assessment
        total_sections = sum(len(result.get("problematic_sections", [])) for result in layer_scores.values())
        complexity_score = 1.0
        
        if total_sections <= 2:
            complexity_score = 1.0  # Simple fixes
        elif total_sections <= 4:
            complexity_score = 0.8  # Moderate complexity
        else:
            complexity_score = 0.6  # High complexity - more risky
        
        trust_factors.append(("fix_complexity", complexity_score, 0.3))
        
        # 3. Issue severity assessment
        severe_issues = 0
        total_issues = 0
        
        for layer, result in layer_scores.items():
            for section in result.get("problematic_sections", []):
                total_issues += 1
                issue_text = section.get("issue", "").lower()
                # Check for severe issues that require human review
                if any(keyword in issue_text for keyword in [
                    "factual error", "contradiction", "misleading", "incorrect",
                    "harmful", "unsafe", "inappropriate", "citation missing"
                ]):
                    severe_issues += 1
        
        if total_issues > 0:
            severity_score = 1.0 - (severe_issues / total_issues) * 0.5
        else:
            severity_score = 1.0
        
        trust_factors.append(("issue_severity", severity_score, 0.2))
        
        # 4. Historical success rate (simulated for now)
        # In a real implementation, this would track fix success rates
        historical_success = 0.85  # Default baseline
        trust_factors.append(("historical_success", historical_success, 0.1))
        
        # Calculate weighted trust score
        weighted_score = sum(score * weight for _, score, weight in trust_factors)
        
        # Apply threshold-based adjustments
        if weighted_score >= 0.85:
            # High trust - boost slightly for auto-approval
            final_trust = min(1.0, weighted_score * 1.05)
        elif weighted_score >= 0.7:
            # Medium trust - neutral
            final_trust = weighted_score
        else:
            # Low trust - penalize more heavily
            final_trust = max(0.5, weighted_score * 0.9)
        
        return final_trust
    
    def should_auto_apply_fixes(self, qa_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determine whether fixes should be applied automatically based on trust scoring
        Returns decision with reasoning
        """
        confidence = qa_results.get("confidence", 0.0)
        overall_score = qa_results.get("overall_score", 0.0)
        total_sections = len(qa_results.get("inaccurate_or_confusing_sections", []))
        
        # Get trust components for detailed reasoning
        layer_scores = qa_results.get("layer_scores", {})
        trust_score = self._calculate_trust_score(layer_scores) if layer_scores else 0.5
        
        # Decision thresholds (more lenient for manual QA)
        auto_apply_threshold = 0.8
        suggest_threshold = 0.4  # Lowered from 0.6 to allow more manual fixes
        max_sections_auto = self.config.get("max_sections", 5)
        
        decision = {
            "auto_apply": False,
            "suggest_review": False,
            "manual_review_required": False,
            "reasoning": [],
            "confidence_score": confidence,
            "trust_score": trust_score,
            "overall_quality": overall_score
        }
        
        # Apply decision logic
        if (confidence >= auto_apply_threshold and 
            overall_score >= 0.7 and 
            total_sections <= max_sections_auto and
            trust_score >= 0.8):
            decision["auto_apply"] = True
            decision["reasoning"].append(f"High confidence ({confidence:.2f}) and trust ({trust_score:.2f})")
            decision["reasoning"].append(f"Limited scope ({total_sections} sections)")
            decision["reasoning"].append(f"Good base quality ({overall_score:.2f})")
            
        elif (confidence >= suggest_threshold and 
              overall_score >= 0.6 and 
              total_sections <= max_sections_auto * 2):
            decision["suggest_review"] = True
            decision["reasoning"].append(f"Moderate confidence ({confidence:.2f})")
            decision["reasoning"].append("Suitable for review and approval")
            if trust_score < 0.8:
                decision["reasoning"].append(f"Trust score needs attention ({trust_score:.2f})")
                
        else:
            decision["manual_review_required"] = True
            decision["reasoning"].append("Manual review required due to:")
            if confidence < suggest_threshold:
                decision["reasoning"].append(f"• Low confidence score ({confidence:.2f})")
            if overall_score < 0.6:
                decision["reasoning"].append(f"• Poor base quality ({overall_score:.2f})")
            if total_sections > max_sections_auto * 2:
                decision["reasoning"].append(f"• Too many issues ({total_sections} sections)")
            if trust_score < 0.6:
                decision["reasoning"].append(f"• Low trust score ({trust_score:.2f})")
        
        return decision


class ReportImprovementPipeline:
    """Automated pipeline for improving reports based on QA feedback"""
    
    def __init__(self, qa_system: ReportQASystem, max_iterations: int = 2):
        self.qa_system = qa_system
        self.max_iterations = max_iterations
    
    def improve_report(self, report_content: str, sources: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
        """
        Run complete improvement pipeline: QA -> Fix -> Re-QA
        """
        # Step 1: Initial QA
        initial_qa = self.qa_system.run_report_qa(report_content, sources, query)
        
        if not initial_qa.get("auto_fix_recommended", False):
            return {
                "status": "no_auto_fix",
                "original_report": report_content,
                "improved_report": report_content,
                "qa_results": initial_qa,
                "improvements_made": []
            }
        
        # Step 2: Apply fixes
        improved_report, improvements_made = self._apply_fixes(
            report_content, 
            initial_qa["inaccurate_or_confusing_sections"],
            sources,
            query
        )
        
        # Step 3: Re-run QA on improved report
        final_qa = self.qa_system.run_report_qa(improved_report, sources, query)
        
        return {
            "status": "improved",
            "original_report": report_content,
            "improved_report": improved_report,
            "initial_qa": initial_qa,
            "final_qa": final_qa,
            "improvements_made": improvements_made,
            "score_improvement": final_qa["overall_score"] - initial_qa["overall_score"]
        }
    
    def improve_report_iterative(self, report_content: str, sources: List[Dict[str, Any]], 
                                query: str, target_score: float = 0.85) -> Dict[str, Any]:
        """
        Iteratively improve report until target score is reached or max iterations exceeded
        """
        current_report = report_content
        all_improvements = []
        iteration_history = []
        
        for iteration in range(self.max_iterations):
            # Run QA on current version
            qa_result = self.qa_system.run_report_qa(current_report, sources, query)
            
            iteration_data = {
                "iteration": iteration + 1,
                "qa_score": qa_result["overall_score"],
                "issues_found": len(qa_result["inaccurate_or_confusing_sections"]),
                "improvements_applied": 0
            }
            
            # Check if we've reached the target score
            if qa_result["overall_score"] >= target_score:
                iteration_data["status"] = "target_reached"
                iteration_history.append(iteration_data)
                break
            
            # Check if auto-fix is recommended
            if not qa_result.get("auto_fix_recommended", False):
                iteration_data["status"] = "no_auto_fix"
                iteration_history.append(iteration_data)
                break
            
            # Apply fixes
            improved_report, improvements_made = self._apply_fixes(
                current_report, 
                qa_result["inaccurate_or_confusing_sections"],
                sources,
                query
            )
            
            # Check if any improvements were actually made
            if improved_report == current_report or not improvements_made:
                iteration_data["status"] = "no_improvements"
                iteration_history.append(iteration_data)
                break
            
            current_report = improved_report
            all_improvements.extend(improvements_made)
            iteration_data["improvements_applied"] = len(improvements_made)
            iteration_data["status"] = "improved"
            iteration_history.append(iteration_data)
        
        # Final QA
        final_qa = self.qa_system.run_report_qa(current_report, sources, query)
        
        return {
            "status": "iterative_improvement_complete",
            "original_report": report_content,
            "improved_report": current_report,
            "initial_score": iteration_history[0]["qa_score"] if iteration_history else 0.0,
            "final_score": final_qa["overall_score"],
            "target_score": target_score,
            "iterations_used": len(iteration_history),
            "max_iterations": self.max_iterations,
            "iteration_history": iteration_history,
            "all_improvements": all_improvements,
            "final_qa": final_qa,
            "score_improvement": final_qa["overall_score"] - (iteration_history[0]["qa_score"] if iteration_history else 0.0)
        }
    
    def _apply_fixes(self, report_content: str, problematic_sections: List[Dict[str, Any]], 
                    sources: List[Dict[str, Any]], query: str) -> Tuple[str, List[Dict[str, Any]]]:
        """Apply fixes to problematic sections"""
        
        improved_report = report_content
        improvements_made = []
        
        # Group sections by section_title to avoid conflicts
        sections_to_fix = {}
        for section_issue in problematic_sections:
            section_title = section_issue.get("section_title", "Unknown")
            if section_title not in sections_to_fix:
                sections_to_fix[section_title] = []
            sections_to_fix[section_title].append(section_issue)
        
        # Process each section
        for section_title, issues in sections_to_fix.items():
            if len(improvements_made) >= self.qa_system.config.get("max_sections", 5):
                break
            
            # Extract current section content
            section_content = self._extract_section_content(improved_report, section_title)
            if not section_content:
                continue
            
            # Generate improved section
            improved_section = self._rewrite_section(
                section_title, section_content, issues, sources, query
            )
            
            if improved_section and improved_section != section_content:
                # Replace section in report
                improved_report = self._replace_section_content(
                    improved_report, section_title, improved_section
                )
                
                improvements_made.append({
                    "section": section_title,
                    "issues_addressed": [issue.get("issue", "") for issue in issues],
                    "original_length": len(section_content),
                    "improved_length": len(improved_section)
                })
        
        return improved_report, improvements_made
    
    def _extract_section_content(self, report_content: str, section_title: str) -> str:
        """Extract content of a specific section from the report"""
        lines = report_content.split('\n')
        section_lines = []
        in_section = False
        
        for line in lines:
            # Check if this is the start of our target section
            if line.startswith('##') and section_title.lower() in line.lower():
                in_section = True
                continue
            
            # Check if we've reached the next section
            elif line.startswith('##') and in_section:
                break
            
            # Collect lines if we're in the target section
            elif in_section:
                section_lines.append(line)
        
        return '\n'.join(section_lines).strip()
    
    def _replace_section_content(self, report_content: str, section_title: str, new_content: str) -> str:
        """Replace the content of a specific section in the report"""
        lines = report_content.split('\n')
        result_lines = []
        in_section = False
        
        for line in lines:
            # Check if this is the start of our target section
            if line.startswith('##') and section_title.lower() in line.lower():
                in_section = True
                result_lines.append(line)  # Keep the header
                result_lines.append(new_content)  # Add new content
                continue
            
            # Check if we've reached the next section
            elif line.startswith('##') and in_section:
                in_section = False
                result_lines.append(line)  # Add the next section header
            
            # Add lines if we're not in the target section
            elif not in_section:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def _rewrite_section(self, section_title: str, section_content: str, 
                        issues: List[Dict[str, Any]], sources: List[Dict[str, Any]], 
                        query: str) -> str:
        """Rewrite a section to address identified issues"""
        
        # Prepare issue context
        issue_descriptions = []
        suggested_fixes = []
        
        for issue in issues:
            issue_descriptions.append(issue.get("issue", ""))
            if issue.get("suggested_fix"):
                suggested_fixes.append(issue.get("suggested_fix"))
        
        # Prepare relevant sources
        source_context = ""
        for i, source in enumerate(sources[:3]):
            source_context += f"Source [{i+1}]: {source.get('title', 'Untitled')}\n"
            source_context += f"{source.get('content', {}).get('body', '')[:300]}...\n\n"
        
        prompt = f"""Rewrite the following section to address the identified issues:

Original Query: {query}
Section Title: {section_title}

Current Section Content:
{section_content}

Issues to Address:
{chr(10).join(f"- {issue}" for issue in issue_descriptions)}

Suggested Improvements:
{chr(10).join(f"- {fix}" for fix in suggested_fixes)}

Available Sources:
{source_context}

Please rewrite the section to:
1. Address all identified issues
2. Maintain the same general structure and length
3. Include proper citations [1], [2], etc. when referencing sources
4. Ensure accuracy and clarity
5. Keep the tone consistent with the rest of the report

Return only the improved section content (without the section header)."""
        
        try:
            improved_content = _call_llm_api(prompt, f"section improvement: {section_title}")
            return improved_content.strip() if improved_content else section_content
        except Exception as e:
            print(f"Error improving section {section_title}: {e}")
            return section_content


# Configuration presets
QA_CONFIGS = {
    "basic": {
        "enabled": True,
        "mode": "auto",
        "max_sections": 3,
        "confidence_threshold": 0.8,
        "layers": ["accuracy", "clarity"]
    },
    "comprehensive": {
        "enabled": True,
        "mode": "auto",
        "max_sections": 5,
        "confidence_threshold": 0.7,
        "layers": ["structure", "clarity", "accuracy", "tone"]
    },
    "trust_focused": {
        "enabled": True,
        "mode": "auto",
        "max_sections": 4,
        "confidence_threshold": 0.8,
        "layers": ["accuracy", "clarity", "structure"],
        "trust_threshold": 0.85,
        "conservative_mode": True
    },
    "suggest_only": {
        "enabled": True,
        "mode": "suggest_only",
        "max_sections": 10,
        "confidence_threshold": 0.5,
        "layers": ["structure", "clarity", "accuracy", "tone"]
    },
    "disabled": {
        "enabled": False
    }
}