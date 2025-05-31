# Research Tasks

## Task 1: Environment Setup & Model Configuration
**ID:** task_1
**Objective:** Prepare the local environment for running the QWEN3 30b model using LM Studio and Python libraries.
**Scope:** Install LM Studio, configure QWEN3 30b with 32k context, set up Python runtime, and validate API access to the model.
**Complexity:** medium
**Estimated Documents:** 4

---

## Task 2: FreshService API Integration
**ID:** task_2
**Objective:** Establish secure communication between the AI agent and FreshService instances.
**Scope:** Create Python scripts to handle authentication (instance URL, API key), ticket creation/updating, and status tracking via REST API.
**Complexity:** medium
**Estimated Documents:** 3
**Dependencies:** task_1

---

## Task 3: Ticket Classification Logic Development
**ID:** task_3
**Objective:** Implement NLP-based ticket categorization using the QWEN3 model.
**Scope:** Train/define prompts for IT-related categories (device troubleshooting, software issues, etc.), and integrate confidence scoring for escalation decisions.
**Complexity:** high
**Estimated Documents:** 5
**Dependencies:** task_1, task_2

---

## Task 4: Triage Workflow Implementation
**ID:** task_4
**Objective:** Automate ticket escalation to human agents based on confidence thresholds.
**Scope:** Define rules for low-confidence responses (e.g., <70% accuracy), trigger API updates to mark tickets as 'escalated', and assign to specific agent queues.
**Complexity:** medium
**Estimated Documents:** 3
**Dependencies:** task_3, task_2

---

## Task 5: Testing & Validation
**ID:** task_5
**Objective:** Ensure reliability of classification and triage processes across client scenarios.
**Scope:** Test with sample tickets covering IT categories, validate confidence thresholds, and verify API interactions with FreshService.
**Complexity:** high
**Estimated Documents:** 5
**Dependencies:** task_4, task_3

---

## Task 6: Documentation & Deployment Setup
**ID:** task_6
**Objective:** Prepare deployment instructions and client-specific configuration guides.
**Scope:** Create setup manuals for LM Studio, Python scripts, and guidelines for modifying instance URLs/API keys per client.
**Complexity:** low
**Estimated Documents:** 3
**Dependencies:** task_5

---
