# Modelling Strategy and Implementation

This document provides a detailed summary of the modelling approach used to create the automated math solution verifier. The primary objective is to classify a given solution to a math word problem into one of three categories: `correct`, `conceptual_error`, or `computational_error`.

Our final implementation is a hybrid system that orchestrates two specialized, fine-tuned Large Language Models (LLMs) with a deterministic programmatic evaluation step. This design was chosen after initial experiments with a single, multi-class generative model proved to be unreliable, particularly in identifying computational errors with the required precision.

## Design Philosophy: A Hybrid, Task-Specific Approach

Our initial approach was to try the direct, "natural" approach for our problem: we fine-tuned an LLM (~4B params) to perform the desired three-way classification. That is, the model was tasked with analyzing the problem and solution, and then generating one of the three labels. While this method showed some promise for identifying correct solutions and obvious conceptual flaws, it consistently failed to identify  calculation mistakes (especially with more complicated calculations involving more than two operands, or large operands).

To address these limitations, we redesigned the problem as a pipeline of more narrowly defined tasks. This hybrid approach seeks to take advantage of the semantic understanding capabilities of LLMs while delegating the objective task of arithmetic verification to programmatic logic. Thus, we broke the problem down into two components:

1. **Conceptual Error Detection:** A binary classification model to determine if the overall logic and setup of the solution are sound.
2. **Computational Error Detection:** A generative model to extract every calculation from a solution, which are then programmatically evaluated for correctness.

---

## Component 1: Conceptual Error Detection

This component acts as the first-stage classifier, providing a holistic assessment of the solution's logic.

* **Model:** We chose **`microsoft/Phi-4-mini-instruct`**, a capable 4-billion-parameter model.
* **Architecture:** This component was framed as a binary sequence classification task (`correct` vs. `flawed`). We implemented a custom `GPTSequenceClassifier` class in PyTorch, which consists of:
    1. The `Phi-4` backbone, with LoRA adapters applied to all linear layers for fine-tuning.
    2. A single `torch.nn.Linear` layer as the classification head, which takes the final hidden state for the last token in the input to the base model and projects it to the two output labels. 
* **Fine-Tuning Strategy:** The model was fine-tuned for 5 epochs. We included an early stopping callback that monitored validation accuracy, configured to save only the best-performing checkpoint. This prevented overfitting and ensured the final model generalized well.
* **Training time:** ~1 hour on an NVIDIA A100 GPU (40GB VRAM) via Google Colab
* **Performance:** The fine-tuned classifier achieved a final accuracy of **92.3%** on the held-out test set. (Note: since we attached a classifier head with randomly initialized weights, it did not make sense to try to establish a baseline evaluation before the fine-tuning, so we ommitted this.)

---

## Component 2: Computational Error Detection

### 2.1. Equation Extraction

The goal of this stage is to train a model that can read a line of a mathematical solution and transcribe any equation it contains literally, without interpretation or correction.

* **Model:** We selected **`unsloth/gemma-3-1b-it-unsloth-bnb-4bit`**. A 1-billion-parameter model is sufficiently powerful for this focused transcription task while remaining lightweight and efficient for fine-tuning and inference.
* **Fine-Tuning Strategy:** The model was fine-tuned using Parameter-Efficient Fine-Tuning (PEFT) with LoRA adapters, accelerated by the Unsloth library. The key objective was to teach the model a strict transcription task. The system prompt explicitly instructs the model to:
    * Transcribe the equation exactly as it appears, preserving any mathematical errors.
    * Isolate the equation from all surrounding text and symbols.
    * Wrap the final output in `<eq>` and `</eq>` tags for easy parsing.
* **Training time:** ~5 minutes on an NVIDIA A100 GPU (40GB VRAM) via Google Colab
* **Performance:** The effectiveness of this fine-tuning was significant. The baseline (zero-shot) model achieved a "rigorous score" (a custom metric checking for mathematical and structural equivalence, more or less equivalent to accuracy) of **0.474**. After one epoch of fine-tuning, the model's score on the same test set increased to **0.948**.

### 2.2. Programmatic Evaluation

Once the equations are extracted, they are passed to a simple, deterministic Python function.

* **Logic:** For each extracted equation string (e.g., `"5000-4000=100"`), the function splits the string at the equals sign. It then uses Python's `eval()` to compute the value of the left-hand side and compares it to the value on the right-hand side.
* **Outcome:** The function reports whether any incorrect calculation was found. This programmatic check is infallible and provides the precision that a purely generative approach lacks.

---

## Integrated Pipeline and Final Performance

The two components are orchestrated into a single, cohesive "solution verifier" as demonstrated in the `final-testing` notebook. The logic proceeds as follows:

1. **Stage 1: Conceptual Check.** The full problem and solution are passed to the `Conceptual Error Detection` model (fine-tuned Phi-4), which provides a preliminary verdict of `correct` or `flawed`. This step happens very fast (usually in less than 2 seconds)
2. **Stage 2: Computational Check.** Next, the solution is processed by the `Computational Error Detection` pipeline. The fine-tuned Gemma-3 model extracts all equations, which are then programmatically evaluated for correctness.
3. **Final Verdict Logic.** The final classification is determined by a clear decision hierarchy:
    * If the programmatic evaluation from Stage 2 finds **any** mathematical error, the final verdict is **`computational_error`**. This result has the highest priority and overrides the conceptual model's output.
    * If and only if all calculations are correct, the verdict from the conceptual classifier in Stage 1 (`correct` or `conceptual_error`) is used as the final answer.

This integrated system was evaluated on two test sets, achieving a weighted F1-score of **0.78** on a manually curated test set and **0.82** on the original test split from the training data. This performance validates the effectiveness of the hybrid design, which successfully combines the semantic reasoning of LLMs with the precision of programmatic logic.

**Note on hardware:** The pipeline with both models was tested on a standard Google Colab instance equipped with a single 14GB NVIDIA T4 GPU (this is also the backend for our Huggingface Spaces App). Together, the models take up less than 6 GB of VRAM, so we expect that the pipeline can be run on a large share of laptops.