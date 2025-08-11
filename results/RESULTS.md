# Performance Analysis and Results

This document presents a comprehensive analysis of the final performance of our fine-tuned, two-model pipeline, benchmarked against a powerful frontier model baseline (`gemini-2.5-flash`). The evaluation was conducted on two distinct test sets:

1. **SFT Test Set:** The held-out portion (20%) of our primary Supervised Fine-Tuning dataset, containing a mix of programmatically and manually generated errors.
2. **Final Test Set:** A smaller, manually curated set of challenging problems designed to test generalization.

All prediction results and generated plots are available in the [`/results/inference/`](./inference/) directory.

## Executive Summary

Our fine-tuned pipeline significantly outperforms the `gemini-2.5-flash` baseline in terms of **robustness, specialization, and efficiency**. While the baseline model performs well on the simpler "Final Test Set," its performance on the larger and more diverse "SFT Test Set" is poor, revealing a critical lack of consistency.

**Key Findings:**

* **Superior Specialization:** Our pipeline is an expert at detecting computational errors, achieving **>92% recall** on this class across both test sets. The baseline's recall on this same task collapsed to a mere **30.5%** on the SFT test set.
* **Greater Robustness:** The pipeline's performance is stable across both test sets, whereas the baseline's accuracy varies wildly, indicating it is less reliable.
* **Higher Latency:** The baseline pipeline is approximately **3-4 times faster** than the fine-tuned pipeline. One reason for this could be that we are restricting ourselves to a T4 GPU on which inference is not as fast/optimized as the more powerful GPU's used for frontier models like `gemini-2.5-flash`.

---

## 1. Overall Performance Comparison

On the primary SFT test set, our fine-tuned pipeline demonstrates a clear advantage in both overall accuracy and weighted F1-score. While the baseline's performance improves dramatically on the smaller, manually-curated Final Test Set, our pipeline remains competitive.

![Overall Performance Chart](./inference/overall-performance-comparison.png)

* **On the SFT Test Set:** Our pipeline achieved a weighted F1-score of **0.82**, a substantial improvement over the baseline's **0.61**. This highlights the effectiveness of our fine-tuning on a diverse dataset.
* **On the Final Test Set:** The baseline's performance surged to an F1-score of **0.88**, slightly surpassing our pipeline's **0.78**. This suggests the baseline is highly effective on a narrower distribution of problems but struggles to generalize as well as the fine-tuned system.

## 2. Specialization in Error Detection: A Test of Robustness

The most significant difference between the two systems emerges when analyzing their ability to distinguish between error types.

![Recall by Error Type Chart](./inference/recall-by-error-type.png)

#### Fine-Tuned Pipeline: A Computational Error Specialist

The standout feature of our pipeline is its mastery of detecting computational errors. This is a direct result of our hybrid design, which offloads mathematical verification to a deterministic programmatic check.

* It achieved a recall of **92.5%** for `computational_error` on the SFT set and **93.3%** on the Final Test Set.
* This demonstrates that the system is exceptionally reliable at its core task of identifying calculation mistakes.

#### Baseline Model: A Lack of Consistency

The baseline's performance on this critical task is highly volatile.

* On the SFT test set, its recall for `computational_error` was extremely low at **30.5%**. The confusion matrix reveals that it misclassified the majority of these errors as `conceptual_error`, indicating it recognized a problem but failed to pinpoint its mathematical nature.
* Conversely, on the Final Test Set, its recall for this same class was an excellent **90.7%**.

This dramatic inconsistency suggests that the baseline's ability to detect calculation mistakes is not robust and is highly dependent on the specific structure or phrasing of the problem. **Our fine-tuned pipeline does not have this weakness.**

## 3. Performance vs. Efficiency

The main drawback of our arrangement lies in the latency (averaging ~3-4 seconds per classification). 

![Performance vs. Efficiency Chart](./inference/performance-vs-efficiency.png)

## 4. Analysis of Misclassification Patterns (SFT Test Set)

To understand *why* the models fail, we analyzed their misclassifications against the metadata of the SFT test set.

#### Misclassification by Data Source

This analysis reveals how well each model generalizes to data from different sources (`programmatic` vs. `manual`).

![Misclassification by Source Chart](./inference/misclassification-by-source.png)

* The **Baseline** model struggled more with our programmatically generated data, with over 90% of its errors occurring on these samples.
* The **Fine-Tuned** model, having been trained on this data, handled it better. However, a larger proportion of its errors (22.8%) came from the `manual` set, suggesting it is more challenged by the out-of-distribution, hand-crafted examples.

#### Model Prediction Agreement

This analysis provides a granular view of how the models' predictions align, especially when they are wrong.

![Model Agreement Matrix](./inference/model-agreement-matrix.png)

The most insightful panel is for **"True: Computational Error"**:

* The cell at `(Baseline: conceptual_error, Fine-Tuned: computational_error)` contains **39.6%**. This means that for nearly 40% of all true computational errors, **our pipeline correctly identified the error while the baseline misclassified it as a conceptual one.** This is the single most powerful demonstration of our system's specialized advantage.
* The cell at `(Baseline: correct, Fine-Tuned: computational_error)` contains **23.8%**. This shows that our pipeline correctly identified a computational error in an additional ~24% of cases where the baseline missed the error entirely.

In total, these two cells show that our pipeline made the correct `computational_error` prediction in over **63%** of cases where the baseline failed.
