# Technical Details of Model Fine-Tuning

This document provides a technical deep-dive into the core methodologies and specific implementations used for fine-tuning the two models in our pipeline: the `Phi-4` error classifier and the `Gemma-3` equation extractor.

## Core Methodologies

While the two models perform different tasks, their training is based on the same foundational techniques: Parameter-Efficient Fine-Tuning (PEFT) and 4-bit quantization. These methods allow us to efficiently adapt large models on consumer-grade hardware.

### 1. Parameter-Efficient Fine-Tuning (PEFT) with LoRA

Full fine-tuning of a Large Language Model (LLM), which involves updating all of its billions of parameters, is computationally expensive and requires significant GPU memory. PEFT methods offer a solution by freezing the vast majority of the pre-trained model's weights and only training a small number of new, added parameters.

We use **Low-Rank Adaptation (LoRA)**, a popular and effective PEFT technique. LoRA involves injecting small, trainable "adapter" matrices into the transformer layers of the pre-trained model.

#### The Mathematics of LoRA

To understand LoRA, consider a single, large weight matrix $W_0$ in a pre-trained model (e.g., in a self-attention block). Let its dimensions be $d \times k$. Full fine-tuning would update this matrix by adding a change, $\Delta W$, resulting in a new matrix $W = W_0 + \Delta W$.

The key hypothesis of LoRA is that this change, $\Delta W$, can be effectively approximated by a **low-rank decomposition**. This assumes that the necessary updates for adapting the model to a new task lie on a much lower-dimensional manifold within the vast space of all possible weight changes.

LoRA operationalizes this by representing the large $d \times k$ matrix $\Delta W$ as the product of two much smaller matrices, $B$ and $A$:

$$
\Delta W \approx B \cdot A
$$

Where:
-   Matrix $A$ (dimensions $r \times k$) acts as a **projection**, mapping the original high-dimensional input activations down into a low-dimensional space of rank $r$.
-   Matrix $B$ (dimensions $d \times r$) acts as an **embedding**, mapping the low-rank representation back up into the original high-dimensional output space.
-   The rank `r` is a small integer (e.g., 8, 16, 32) and is the most important LoRA hyperparameter. Since $r \ll d$ and $r \ll k$, the number of parameters in $A$ and $B$ is vastly smaller than in $\Delta W$.

The forward pass of a LoRA-adapted layer is then modified. For an input vector $x$, the output $h$ is calculated as:

$$
h = W_0 x + (\Delta W) x = W_0 x + (B \cdot A) x
$$

During training, the original weight matrix $W_0$ remains frozen. Only the parameters of matrices $A$ and $B$ are trained. A scaling factor, `lora_alpha / r`, is often applied to the adapter's output to control the magnitude of the change: $h = W_0 x + (\frac{\alpha}{r}) B A x$.

At inference time, the trained adapter matrices can be mathematically merged back into the original weights: $W = W_0 + B \cdot A$. This results in a single matrix $W$ with the same dimensions as the original, meaning **LoRA introduces no additional inference latency**.

### 2. 4-Bit Quantization

Quantization is the process of representing numbers with less precision to reduce memory usage. By loading our models in 4-bit precision, we dramatically decrease their memory footprint, making it possible to train them on a single GPU.

#### The World of Data Types

Several data types are involved in the training process, each serving a specific role:

*   **FP32 (32-bit Floating Point):** Full precision. This is the standard for most numerical computations but is memory-intensive. A 1-billion parameter model would require 4 GB of GPU RAM just for the weights in FP32.
*   **FP16 / BF16 (16-bit Half Precision):** These formats use half the memory of FP32. `bfloat16` (BF16) is generally preferred for training as it has a wider dynamic range, which helps prevent gradients from becoming zero ("underflow").
*   **NF4 (4-bit NormalFloat):** A specialized 4-bit format from the bitsandbytes library. It is designed to optimally represent weights that are normally distributed, which is typical for deep learning models.

The interaction between these types is key:
1.  **Storage:** The model's main weights are **stored** in the memory-efficient 4-bit **NF4** format.
2.  **Computation:** During a forward or backward pass, these 4-bit weights are temporarily **de-quantized** to a higher-precision format (we use **BF16**) for the actual matrix multiplications.
3.  **Gradients:** The gradients and optimizer states are also kept in **BF16** to maintain precision during the weight update calculations.

This strategy provides the best of both worlds: a massive reduction in memory for storing the model, combined with the numerical stability required for effective training.

---

## Fine-Tuning Task 1: Conceptual Error Classification (Phi-4)

### Task: A Discriminative Approach to Classification

The goal is to classify a given math solution as either `correct` or `flawed`. We approach this using a **discriminative model**, a classic and highly effective strategy for classification.

Instead of asking the LLM to *generate* the word "correct" or "flawed", we use it as a sophisticated **feature extractor**. The LLM's job is to read the input text and convert it into a single, high-dimensional vector that summarizes all the semantic information relevant to the classification task. A simple linear classifier then learns a decision boundary in this feature space to separate the two classes.

### Model Architecture: Backbone + Classification Head

We use a custom `GPTSequenceClassifier` class that formalizes this discriminative approach.
1.  **The Backbone:** The `microsoft/Phi-4-mini-instruct` model, with LoRA adapters injected for fine-tuning. Its role is to act as the powerful feature extractor.
2.  **The Head:** A single, trainable `torch.nn.Linear` layer. Its role is to act as a simple linear classifier, drawing a hyperplane to separate the feature vectors produced by the backbone.

The data flows through this architecture in a specific sequence during the `forward` pass:
1.  **Get Hidden States:** The input text is passed through the Phi-4 backbone. We extract the hidden states from the final layer of the transformer. This results in a tensor of shape `(batch_size, sequence_length, hidden_size)`.
2.  **Pooling:** To get a single feature vector representing the entire sequence, we use **last-token pooling**. We select the hidden state corresponding to the very last token (`last_hidden_state[:, -1, :]`). This single pooled vector is the final feature representation. The goal of fine-tuning is to train the LoRA adapters to produce a vector that effectively **encodes the model's verdict** on the solution's validity.
3.  **Classification:** This feature vector is passed through the `nn.Linear` head, which projects it down to 2 dimensions (one for each class), producing the final `logits`.

### Loss Calculation: Training for Linear Separability

During training, the `logits` are compared to the true labels using the **Cross-Entropy Loss** function. By backpropagating this loss, the training process simultaneously updates the linear head to find the best decision boundary and adjusts the LoRA adapters in the backbone to produce feature vectors that are more **linearly separable**. In essence, we are teaching the LLM to arrange its output vectors in a way that makes the "correct" and "flawed" examples easy to distinguish with a simple linear cut.

### Tooling: Standard Hugging Face Ecosystem

This task is implemented using the standard Hugging Face libraries: `transformers`, `peft`, and `trl`.

---

## Fine-Tuning Task 2: Equation Extraction (Gemma-3)

### Task: Conditional Text Generation

The goal is to read a line from a math solution and generate the equation it contains. This is a sequence-to-sequence task, where the model must generate a new text sequence based on the input text.

### Model Architecture: Standard Generative Model

Unlike the classifier, this model does **not** have a custom head. We use the `unsloth/gemma-3-1b-it-unsloth-bnb-4bit` model in its standard generative configuration. The fine-tuning process directly updates the model's existing language modeling head via LoRA adapters.

### Loss Calculation: Causal Language Modeling Loss

The loss function is the standard **Causal Language Modeling (CLM)** loss. For each token in the target output sequence (e.g., `<eq>2+2=4</eq>`), the model predicts the next token. The loss is calculated by comparing the model's predicted probability distribution with the actual next token.

A crucial technique used here is **training on responses only**. We mask the loss calculation so that the model is only penalized for its predictions on the assistant's part of the conversation (the equation), not for its predictions on the input prompt. This makes training much more efficient.

### Tooling: Unsloth for Accelerated Training

This task leverages the **Unsloth** library, a powerful tool designed to dramatically accelerate LoRA fine-tuning. Unsloth achieves this by implementing custom, highly-optimized CUDA kernels and efficient memory management, resulting in significantly faster training times and lower VRAM usage compared to a standard implementation.

---

## Summary Comparison Table

For a quick overview, this table highlights the key differences between the two fine-tuning tasks.

| Aspect | Error Classification (Phi-4) | Equation Extraction (Gemma-3) |
| :--- | :--- | :--- |
| **Core Task** | **Discriminative** (Binary Classification) | **Generative** (Text Generation) |
| **Model Architecture**| Backbone + Custom Classification Head | Standard Generative Model (No custom head) |
| **Loss Function** | Cross-Entropy on a single pooled vector | Causal LM Loss on a sequence of tokens |
| **Loss Masking** | N/A | Loss calculated on *assistant's response only* |
| **Primary Library** | Standard Hugging Face `trl` & `peft` | **Unsloth** for accelerated training |