# **Project Verifier: A Product-Focused Strategy for a Winning Demo**

**To:** The Team
**From:** Arvind
**Date:** [Current Date]
**Re:** A Revised Strategy to Maximize Project Impact

## 1. Executive Summary: The Vision

This document outlines a revised, product-oriented strategy for our project. Our previous goal was centered on academic exploration. To maximize our impact for the final presentation and appeal to industry judges, we are pivoting to a more tangible goal: **building a polished, impressive "Proof-of-Thought" solution verifier application.**

The core idea is to create a tool that is not only accurate but also demonstrates sophisticated engineering. This approach shifts our focus from *answering a research question* to *building a compelling product*. This is a more direct path to showcasing our technical skills and is better aligned with the evaluation criteria.

## 2. The Core Idea: A Hybrid LLM-Code Pipeline

The biggest change is moving from a single "end-to-end" model to a smarter, multi-step pipeline that uses the right tool for each job. This demonstrates a much deeper level of system design.

Here's the new workflow:

**Input:** A math problem and a candidate solution.

```
+--------------------------------+
| Step 1: Conceptual Check (LLM) |
| - Is the logic/setup correct?  |
| - IGNORE arithmetic.           |
+--------------------------------+
             |
             V
+--------------------------------+
| Is there a conceptual error?   | --- YES ---> [STOP & Report Conceptual Error]
+--------------------------------+
             |
             NO
             |
             V
+--------------------------------+
| Step 2: Extract Equations(LLM) |
| - LLM parses the text.         |
| - Outputs a dict of equations. |
+--------------------------------+
             |
             V
+--------------------------------+
| Step 3: Verify Arithmetic(Code)|
| - Python evaluates equations.  |
| - Python compares results.     |
| - Python generates verdict.    |
+--------------------------------+
             |
             V
[Final Verdict: Correct or Computational Error]
```

This hybrid approach is powerful because it uses the LLM for what it's good at (understanding language and logic) and uses deterministic Python code for what it's good at (perfect arithmetic).

## 3. The End Goal: Our Streamlit Demo App

The final deliverable will be a clean, interactive web application that showcases our system. This makes our work tangible and easy to understand.

The app will feature:

* **A simple UI:** Two text boxes for the `problem` and `solution`, and a "Verify" button.
* **Pre-loaded Examples:** A dropdown menu with 5-10 curated examples to demonstrate different verification scenarios smoothly during the presentation.
* **A Human-Readable Verdict:** We will parse the model's raw output and display it cleanly (e.g., with colored badges for "Correct" or "Flawed").
* **Full Transparency:** A "Show Raw Output" section that displays the model's actual output (`None`, `L{n}: ...`, or the JSON dictionary), proving our demo is real.

## 4. The Technical Plan: A Two-Task Fine-Tuning Strategy

To power this pipeline, we need to fine-tune a model (or models) to perform two distinct, simpler tasks.

**Task A: Conceptual Check**

* **Goal:** Classify a solution as conceptually sound or flawed.
* **Model Input:** A `[CONCEPTUAL_CHECK]` prompt with the problem and solution.
* **Model Output (Simple String):**
  * `None` if the logic is sound.
  * `L{n}: {explanation}` if a conceptual error is found.

**Task B: Equation Extraction**

* **Goal:** For conceptually sound solutions, extract all calculations.
* **Model Input:** An `[EXTRACT_CALCULATIONS]` prompt with the problem and solution.
* **Model Output (JSON):**
  * A dictionary mapping line numbers to equations, e.g., `{"L1": "10+5=15", "L2": "15*2=30"}`.

*We can either fine-tune one model on a mixed dataset of both tasks or fine-tune two separate, specialized models. The two-model approach is more impressive and likely more performant.*

## 5. The Dataset: A Clear and Achievable Plan

This is our data generation roadmap. It is balanced and appropriately sized for our models and timeline.

| Task                   | Composition                          | # Samples | Target Output Format         |
| ---------------------- | ------------------------------------ | --------- | ---------------------------- |
| **A: Conceptual Check**| 1000 Correct                         | 4,000     | String: `None`               |
|                        | 1000 Computational Errors            |           | String: `None`               |
|                        | 2000 Conceptual Errors               |           | String: `L{n}: {explanation}`|
| **B: Equation Extraction**| 1500 Correct                         | 3,000     | JSON: `{"L1": ..., ...}`     |
|                        | 1500 Computational Errors            |           | JSON: `{"L1": ..., ...}`     |
| **Total**              |                                      | **7,000** |                              |

---

## 6. Comparison of Methodologies: Previous vs. Current Strategy

To ensure clarity, this section outlines the concrete differences between our original research-focused approach and the new product-focused strategy.

| Aspect                | **Previous (Research) Strategy**                                                                                               | **Current (Product) Strategy**                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Goal**      | Investigate if an LLM can be fine-tuned to classify errors based on reasoning text.                                            | Build a working, performant "Solution Verifier" application.                                                                                                |
| **Core Architecture** | A single, end-to-end LLM that takes `(problem, solution)` and outputs a final JSON verdict.                                      | A multi-step pipeline where an LLM first checks for conceptual errors, then extracts equations for programmatic verification by Python code.                |
| **Fine-Tuning Task(s)**| A single fine-tuning task to generate a complex, 4-class JSON object.                                                          | Two distinct fine-tuning tasks: (A) simple string generation for conceptual checks, and (B) JSON dictionary generation for equation extraction.             |
| **Model Output**      | A single, comprehensive JSON object containing the final verdict (`verdict_class`), line number, and explanation.                  | Two potential outputs: either a simple string (`None` or `L{n}: {explanation}`) or a JSON dictionary of equations (`{"L1": "10+5=15", ...}`).                 |
| **Role of Code**      | Primarily for data generation and model evaluation.                                                                            | An active component of the inference pipeline, responsible for evaluating extracted equations and generating the final verdict for computational checks.    |
| **Final Deliverable** | A fine-tuned model and a report analyzing its performance and limitations.                                                      | A deployed Streamlit/Gradio application that provides a live, interactive demo of the verifier system.                                                    |

This pivot represents a fundamental shift from a monolithic model design to a modular, component-based system.

## 7. Required Action Items for Project Completion

To execute this new strategy, the following concrete tasks must be completed. This list serves as our project checklist.

### **A. Data Generation Pipeline (Highest Priority)**

1. **[Modify] `conceptual_error_generator.py`:**
    * Change the target output format for conceptual error samples from a JSON object to the simple string format: `"L{n}: {explanation}"`.
    * **Action:** Update the function that saves the final `(input, target)` pairs.

2. **[Create] `no_conceptual_error_target_generator.py`:**
    * **Task:** For all conceptually sound samples (i.e., the original correct solutions and solutions with only computational errors), the target for the `[CONCEPTUAL_CHECK]` task must be the simple string `"None"`.
    * **Action:** Create a script that iterates through these samples and generates the corresponding `(input, target)` pairs.

3. **[Create] `equation_extraction_target_generator.py`:**
    * **Task:** For all conceptually sound samples, the target for the `[EXTRACT_CALCULATIONS]` task must be a JSON dictionary of equations.
    * **Action:** Create a script that uses the existing calculator annotations (`<<...>>`) in our original data to generate the target dictionaries (e.g., `{"L1": "10+5=15", ...}`). This script should handle cases with no calculations by producing an empty dictionary (`{}`).

4. **[Execute] Full Data Generation:**
    * **Task:** Run the three scripts above to generate the complete, final dataset of ~7,000 samples, split between the two tasks.
    * **Action:** Execute the scripts and save the final training/validation data to a designated location.

### **B. Model Fine-Tuning**

1. **[Modify] `finetune.py`:**
    * **Task:** The script must be able to handle the mixed-task dataset if we choose the single-model approach. It should correctly process the two different prompt prefixes and target formats.
    * **Action:** Update the data loading and formatting logic in the training script.

2. **[Experiment] Model Selection:**
    * **Task:** Decide whether to use a single multi-task model or two specialized models.
    * **Action:** Conduct fine-tuning runs for both scenarios if time permits, or make a final decision based on our complexity/performance trade-off analysis. Save the final model adapter(s).

### **C. Application and Deployment**

1. **[Create] `app.py` (Streamlit/Gradio):**
    * **Task:** Develop the frontend UI for the demo application.
    * **Action:** Implement the UI components: text inputs, "Verify" button, formatted output display, and pre-loaded examples dropdown.

2. **[Create] `pipeline_logic.py`:**
    * **Task:** Implement the backend orchestration logic for the 3-step verification process.
    * **Action:** Write the Python functions that:
        * Take user input and call the `[CONCEPTUAL_CHECK]` model.
        * Parse the model's string output.
        * Conditionally call the `[EXTRACT_CALCULATIONS]` model.
        * Parse the resulting JSON and pass the equations to a safe `eval` function.
        * Programmatically compare results and generate the final, human-readable verdict.

3. **[Deploy] Final Application:**
    * **Task:** Deploy the completed application to a public, shareable URL.
    * **Action:** Set up a Hugging Face Space, upload the application code, and configure it to load the fine-tuned model(s) for a stable demo.

---
