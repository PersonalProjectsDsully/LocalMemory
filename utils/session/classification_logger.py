import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

class ClassificationLogger:
    """Logger for YouTube video classification results"""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / "classification_log.jsonl"
        self.summary_file = self.log_dir / "classification_summary.json"
        
    def log_classification(self, 
                         video_id: str,
                         video_title: str,
                         channel: str,
                         category: str,
                         confidence: str,
                         method: str,
                         summary: Optional[str] = None,
                         original_response: Optional[str] = None) -> None:
        """Log a single classification result"""
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "video_id": video_id,
            "video_title": video_title,
            "channel": channel,
            "category": category,
            "confidence": confidence,
            "method": method
        }
        
        # Add optional fields if provided
        if summary:
            log_entry["summary_preview"] = summary[:200] + "..." if len(summary) > 200 else summary
        if original_response:
            log_entry["original_response"] = original_response
            
        # Append to JSONL file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
            
        # Update summary statistics
        self._update_summary()
    
    def _update_summary(self) -> None:
        """Update summary statistics file"""
        
        # Read all log entries
        entries = []
        if self.log_file.exists():
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entries.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        continue
        
        # Calculate statistics
        total_classifications = len(entries)
        category_counts = {}
        confidence_counts = {"high": 0, "medium": 0, "low": 0}
        method_counts = {}
        
        for entry in entries:
            # Count categories
            category = entry.get('category', 'Unknown')
            category_counts[category] = category_counts.get(category, 0) + 1
            
            # Count confidence levels
            confidence = entry.get('confidence', 'unknown')
            if confidence in confidence_counts:
                confidence_counts[confidence] += 1
            
            # Count methods
            method = entry.get('method', 'unknown')
            method_counts[method] = method_counts.get(method, 0) + 1
        
        # Calculate success rate (high confidence classifications)
        success_rate = (confidence_counts['high'] / total_classifications * 100) if total_classifications > 0 else 0
        
        # Create summary
        summary = {
            "last_updated": datetime.now().isoformat(),
            "total_classifications": total_classifications,
            "success_rate": f"{success_rate:.1f}%",
            "category_distribution": category_counts,
            "confidence_distribution": confidence_counts,
            "method_distribution": method_counts,
            "most_common_category": max(category_counts, key=category_counts.get) if category_counts else None,
            "least_common_category": min(category_counts, key=category_counts.get) if category_counts else None
        }
        
        # Write summary
        with open(self.summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get classification summary statistics"""
        if self.summary_file.exists():
            with open(self.summary_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "last_updated": None,
            "total_classifications": 0,
            "success_rate": "0%",
            "category_distribution": {},
            "confidence_distribution": {},
            "method_distribution": {}
        }
    
    def get_recent_classifications(self, limit: int = 20) -> list:
        """Get recent classification entries"""
        entries = []
        if self.log_file.exists():
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entries.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        continue
        
        # Return most recent entries
        return entries[-limit:] if len(entries) > limit else entries

# Create singleton instance
classification_logger = ClassificationLogger()