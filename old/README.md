# Erdos-DL-June25-Math

## Project Guide: Generating Datasets for Mathematical Reasoning Analysis

This document outlines two potential research projects focused on enhancing the logical reasoning capabilities of Large Language Models (LLMs). Both projects attempt to use a novel, high-rigor data generation pipeline to create specialized datasets for Supervised Fine-Tuning (SFT).

### 1. Project Ideas

The team will choose between two primary research directions:

#### Project Idea 1: The "Problem Validator" Model

* **Summary:** Fine-tune an LLM to classify mathematical word problems as **(1) Solvable**, **(0) Contradictory**, or **(2) Underspecified**.
* **Justification & Relevance:** This project tackles the critical AI safety issue of "hallucination" and "confabulation." By teaching a model to first validate the premises of a problem, we train it to recognize when a question *cannot* or *should not* be answered as posed. This is a form of AI metacognition—the ability to reason about the validity of its inputs—which is essential for creating reliable and trustworthy AI systems that can safely handle flawed or ambiguous user queries.
* **Dataset Requirement:** The training data will consist of `(problem_text, class_label, reasoning_trace)` tuples. The `reasoning_trace` is a natural language chain-of-thought explaining *why* a problem is contradictory or underspecified (e.g., "The calculated total of 10 cows contradicts the stated total of 12 cows.").

#### Project Idea 2: The "Solution Verifier" Model

* **Summary:** Fine-tune an LLM to analyze a mathematical solution trace and classify it as **Correct** or **Flawed**. For flawed solutions, it should further classify the error into a pre-determined category (e.g., `computational_error`, `incorrect_operand`).
* **Justification & Relevance:** This project targets the powerful "AI as a Reviewer" use case. In many real-world applications, the primary task is not to solve from scratch, but to review, debug, or validate an existing line of reasoning. This is a more common and practical scenario. Success in this area would lead to tools that can help students learn, debug scientific models, or audit financial calculations.
* **Dataset Requirement:** The training data will consist of `(correct_problem_text, flawed_solution_trace, error_label_json)` tuples. The `error_label_json` would be a structured object providing details about the flaw, such as `{ "error_type": "incorrect_operation", "line_number": 2, "correction": "Multiplication should be used here, not addition." }`.

---

### 2. Dataset Generation Strategy

For both project ideas, a "perfectly labeled" dataset cannot be generated directly by an LLM without significant risk of annotation errors. Therefore, our strategy is to **first create a ground-truth "oracle" and then programmatically inject errors** to ensure the final labels are 100% accurate.

* **For Idea 1:** We will inject errors into the parameters of the problem statement itself, creating guaranteed contradictions or underspecified scenarios.
* **For Idea 2:** We will inject errors into the steps of the solution trace, creating guaranteed and precisely classifiable flaws in the reasoning process.

---

### 3. Intermediate Step: The "Oracle Factory"

The common link for both project ideas is the creation of a high-confidence, computable representation of the original problem. This is a three-stage validation pipeline that produces a verified Python function—our oracle.

1. **Code Generation:** Multiple independent LLMs are prompted to formalize a GSM8K problem and its solution into a structured Python function.
2. **Validation Pipeline:** These generated functions are subjected to a series of unit tests to find a robust consensus:
    * **UT-1 (Parse & Pre-filter):** All files are parsed, and any that fail to produce the correct final answer on their default arguments are discarded.
    * **UT-2 (Pairwise Alignment):** The script compares every pair of surviving functions. It uses a "bucket and match" strategy, first grouping arguments by `(type, default_value)` and then performing a semantic comparison (using SBERT on argument names and comments) to find the best alignment. This is flexible to naming and ordering differences.
    * **UT-3 (Pairwise Fuzzing):** Each aligned pair is rigorously tested for functional equivalence using the "Fuzz Aligned, Freeze Unaligned" strategy. This proves that their underlying mathematical logic is identical under known constraints.
3. **Confidence Score:** The results are synthesized into a final **Confidence Score**. This score is based on the completeness of the alignment, the semantic clarity of the arguments, and a bonus for the size of the consensus "clique" (the largest group of models that all mutually validate each other). This gives us a quantifiable measure of confidence in our oracle.

---

### 4. Error-Injection Strategy

Once a high-confidence "canonical" function is selected from the validated clique, we inject errors.

### For Idea 1 (Problem Validator)

1. **Action:** Programmatically modify one or more default argument values in the canonical function to create a logical flaw (e.g., `total_fruit = 8` becomes inconsistent with `apples = 6, oranges = 3`).
2. **Propagation:** The modified numerical value is then found and replaced in the original natural language problem text.
3. **Final Dataset:** The output is a `(modified_problem_text, class_label=0, reasoning_trace)` tuple, where the reasoning trace is generated from a template based on the injected flaw.

### For Idea 2 (Solution Verifier)

1. **Action:** Take the original, correct solution trace from the GSM8K dataset.
2. **Injection:** Programmatically introduce a specific, classifiable error into one of the steps. The error types include:
    * **Computational Error:** `2*5 = 10` is changed to `2*5 = 11`.
    * **Incorrect Operand:** `price * quantity` is changed to `price * tax`.
    * **Incorrect Operation:** `price * quantity` is changed to `price + quantity`.
    * **Skipped Step:** A necessary step (e.g., adding tax) is removed from the trace.
3. **Final Dataset:** The output is a `(problem_text, flawed_solution_trace, error_label_json)` tuple.

---

## 5. Supervised Fine-Tuning (SFT)

The fine-tuning process involves training a base LLM on our generated dataset to perform the desired classification task.

* **Process:** We will use a standard Supervised Fine-Tuning (SFT) workflow, likely using the Hugging Face `transformers` and `peft` libraries for efficiency (e.g., using LoRA). The model will be trained to generate a structured JSON output that includes the classification and reasoning.
* **Baselines:** To measure the effectiveness of our fine-tuned model, we will first establish a zero-shot baseline. For either project idea, we will prompt a powerful base model (e.g., GPT-4, Llama 3 70B) with the classification task without any examples and measure its performance. Our goal is for our smaller, fine-tuned model to significantly outperform this baseline.
* **Model Recommendations:** For fine-tuning, we should start with powerful open-source models under 20 billion parameters for faster iteration and lower computational cost. Good candidates include:
  * **Llama 3 8B:** A state-of-the-art, powerful base model with strong reasoning skills.
  * **Mistral 7B Instruct:** Another excellent choice known for its efficiency and strong performance.
  * **Gemma 7B:** Google's open model, also a very capable starting point.

---

## 6. Difficulties and Bottlenecks

A realistic assessment of the challenges is crucial for project planning.

### Shared Difficulties

* **Code Generation & Validation (Primary Bottleneck):** This initial stage is the most complex and costly part of the entire pipeline.
  * **API Costs:** Generating code from multiple LLMs for every problem in the dataset will be the main financial cost.
  * **Rigor vs. Yield:** Our validation pipeline is strict. For many problems, the LLMs may not produce enough high-quality, consistent outputs to form a consensus. This means our final usable dataset might be significantly smaller than the original GSM8K dataset. The `ConfidenceScore` is our main tool for managing this trade-off.

### Difficulties Specific to Idea 1 (Problem Validator)

* **Subtlety of Contradictions:** As discovered with the "cows vs. barn capacity" example, creating a *true, unambiguous* contradiction is harder than it looks. It requires a deep semantic understanding of the problem's structure, which can be difficult to automate. Many naively injected "errors" may not be logical contradictions at all.
* **Reasoning Trace Generation:** Creating the high-quality, natural language chain-of-thought for *why* a problem is flawed is a secondary generation task. This may require its own set of prompts, templates, and quality checks.

### Difficulties Specific to Idea 2 (Solution Verifier)

* **More Controlled, Less Ambiguous:** This path is generally more straightforward. The types of errors are well-defined, and their injection is a more direct, programmatic task.
* **Dependence on Original Trace:** The quality of the final training example depends on the quality of the original solution trace from the GSM8K dataset. If the original trace is convoluted or unclear, injecting a clean error may be difficult.
* **Error Taxonomy:** The team must agree on a finite and comprehensive set of error classifications. This taxonomy must be robust enough to cover most logical failures but simple enough for the model to learn effectively. Deciding on the right level of granularity is a key challenge.
