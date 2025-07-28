# Experiments for academic-oriented project

There are two broad categories:

1. Discriminative: The model is treated as a "feature extractor". That is, the labels (correct, flawed, etc.) are encoded as digits (0, 1 etc.), and a custom classifier head is attached to the model. This classifier head accepts the vector representation of the last token in the models response, and maps this to a probability distribution over the classes. Although this classifier head could be any traditional ML soft classifier, for simplicity we use only a linear (i.e. softmax regression) classifier. Thus, during fine-tuning, when the model weights as well as the classifier head's weights are updated, the model learns to extract features to look like vectors living in linearly separable clusters. Note that the loss function for this type of fine-tuning is cross-entropy using the numerically encoded classes (**not** the token-space).

2. Generative: The model is treated as an auto-completer (i.e. chat assistant) and asked to respond to the prompt in a structured format (typically a json object). This version is simpler in that there is no need for a custom classifier head to be attached, but on the other hand, it is also more sophisticated because the loss function used is the usual "cross-entropy for the next token" loss function on the token-space. Since the models we are testing out (`phi-4-mini-instruct`, `qwen-3-4B`) are already very capable at mathematical reasoning, the main aims of the fine-tuning are to (a) refine the model's understanding of the distinction between conceptual and computational errors (as we are defining them), and (b) ensure the model learns to structure its output in the desired format. 

## 1. Discriminative experiments

### 1.1 Binary classification

#### 1.1.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct or flawed.
- **Labels**: 0 (correct) and 1 (flawed)

#### 1.1.2 Dataset description

Let $A$ denote the subset of GSM8K problems for which there exists a sample with conceptual error (either manually generated, or programmatically generated and then validated by a human), and let $N = |A|$. Then, we choose a subset $B$ of GSM8K problems with these properties:

1. $B$ is disjoint from $A$.
2. $|B| = |A| = N$.
3. For each problem in $B$, there exists a computational-error sample (priority will be given to samples made manually).

Then, the dataset will contain a total of $4N$ samples, with $2N$ distinct problems, chosen as follows:

1. $N$ conceptual error samples for problems in $A$.
2. $N$ computational error samples for problems in $B$.
3. $N$ correct samples for problems in $A$.
4. $N$ correct samples for problems in $B$.

In this way, the dataset will be perfectly balanced between the two classes 0 and 1.

### 1.2 Ternary classification

#### 1.2.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct, or has a computational error, or has a conceptual error.
- **Labels**: 0 (correct), 1 (conceptual error), and 2 (computational error)

#### 1.2.2 Dataset description

Let $A$ denote the subset of GSM8K problems for which there exists a sample with conceptual error (either manually generated, or programmatically generated and then validated by a human), and let $N = |A|$.

Then, the dataset will contain a total of $3N$ samples, with $3$ versions of each of the $N$ problems in $A$:

1. $N$ conceptual error samples.
2. $N$ original, correct samples (drawn from GSM8K).
3. $N$ computational error samples (priority is given first to any manually-generated samples, and then, to the programmatically-generated samples).

Note: A small portion of the problems in $A$ may not have an associated computational-error-sample, in which case they will be pruned out.

In this way, the dataset will be prefectly balanced between the classes 0, 1, and 2.

## 2. Generative experiments

### 2.1 Binary classification

#### 2.1.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct or flawed.
- **Labels**: "correct" and "flawed"

#### 2.1.2 Dataset description

The dataset will be identical to the dataset in 1.1.2; the only changes will be in the formatting of the labels (switching from a discriminative setup to a generative setup).

### 2.2 Ternary classification

#### 2.2.1 Sample description

- **Input**: Consists of a problem along with a solution (correct or flawed), and a minimal prompt directing the model to determine whether the solution is correct, has a conceptual error, or has a computational error.
- **Labels**: "correct", "computational_error", and "conceptual_error"

#### 2.2.2 Dataset description

The dataset will be identical to the dataset in 1.2.2; the only changes will be in the formatting of the labels (switching from a discriminative setup to a generative setup).

### 2.3 Final answer + reasoning classification

#### 2.3.1 Sample description

- **Input**:  Consists of a problem along with a solution (correct or flawed), along with instructions for the model to do the following:
  - Classify the final answer as "correct" or "incorrect"
  - If the final answer is "correct", classify the solution as "complete" (if all relevant reasoning is included) or "missing_step" (if some intermediate (correct) value is used in the reaosning, but the value is never explicitly computed in the solution).
  - If the final answer is "incorrect", classify the solution as "conceptual_error" or "computational_error"
  - Provide the output in the JSON-structured format described below.
- **Label**: Should follow this format:

```text
    ```json
    {
        "final_answer_verdict": "correct" | "incorrect"
        "reasoning_verdict": "complete" or "missing_step" if final answer is correct | "computational_error" or "conceptual_error" if final answer is incorrect
    }
    ```
```

#### 2.3.2 Dataset description

Let $A$ denote the subset of GSM8K problems for which there exists a sample with conceptual error (either manually generated, or programmatically generated and then validated by a human), and let $N = |A|$. Then, we take four versions of each problem in $A$, corresponding to the four possible combinations of "final_answer_verdict" and "reasoning_verdict", resulting in a dataset with $4N$ samples. Thus, there will be $N$ samples of each of the following types:

- "correct" and "complete"
- "correct" and "missing_step"
- "incorrect" and "computational_error"
- "incorrect" and "conceptual_error"

Note: To create the samples with missing steps, we may restrict ourselves to samples with at least 3 solution lines, which would result in some of the problems in $A$ getting pruned out.

### 2.4 Binary classification with erroneous line

#### 2.4.1 Sample description

- **Input**:  Consists of a problem along with a solution (correct or flawed) formatted as a dict mapping the line number ("L1", "L2" etc., with "FA" for the final answer) to the corresponding solution line. The input will also prompt the model to classify the solutions as "correct" or "flawed", identify the (first) line in which it detects an error, and provide its output in the JSON-structured format described below.
- **Label**: Should follow this format:

```text
    ```json
    {
        "verdict": "correct" | "flawed",
        "erroneous_line_number": "L1", "FA" etc. if "verdict" is "flawed" | "NA" if "verdict" is "correct"
    }
    ```
```

#### 2.4.2 Dataset description

Identical to 2.1.2, with the only change being that the assistant content (i.e. the "label") will be put into the desired JSON format and include the erroneous line number.

Note: a small number of samples (for problems in $A$ or $B$) may be missing the erroneous line number (especially the manually generated samples). These problems will be pruned out.

### 2.5 Ternary classification with erroneous line

#### 2.5.1 Sample description

- **Input**:  Consists of a problem along with a solution (correct or flawed) formatted as a dict mapping the line number ("L1", "L2" etc., with "FA" for the final answer) to the corresponding solution line. The input will also prompt the model to classify the solutions as "correct", "conceptual_error" or "computational_error", identify the (first) line in which it detects an error, and provide its output in the JSON-structured format described below.
- **Label**: Should follow this format:

```text
    ```json
    {
        "verdict": "correct" | "conceptual_error" | "computational_error"
        "erroneous_line_number": "L1", "FA" etc. if "verdict" is "flawed" | "NA" if "verdict" is "correct"
    }
    ```
```

#### 2.5.2 Dataset description

Identical to 2.2.2, with the only change being that the assistant content (i.e. the "label") will be put into the desired JSON format and include the erroneous line number.

Note: a small number of samples (for problems in $A$ or $B$) may be missing the erroneous line number (especially the manually generated samples). These problems will be pruned out.

### 2.6 Final answer + reasoning classification with erroneous line

#### 2.6.1 Sample description

- **Input**:  Consists of a problem along with a solution (correct or flawed) formatted as a dict mapping the line number ("L1", "L2" etc., with "FA" for the final answer) to the corresponding solution line. The input will also instruct the model to do carry out the same classification as in 2.3.1, with an added instruction to also include the erroneous line number.
- **Label**: Should follow this format:

```text
    ```json
    {
        "final_answer_verdict": "correct" | "incorrect"
        "reasoning_verdict": "complete" or "missing_step" if final answer is correct | "computational_error" or "conceptual_error" if final answer is incorrect,
        "erroneous_line_number": "L1", "FA" etc. if "final_answer_verdict" is "incorrect" | "NA" if "verdict" is "correct"
    }
    ```
```

#### 2.6.2 Dataset description

Identical to 2.3.2, with the only change being that the assistant content (i.e. the "label") will be put into the desired JSON format and include the erroneous line number.

Note: a small number of samples (for problems in $A$ or $B$) may be missing the erroneous line number (especially the manually generated samples). These problems will be pruned out.

### 2.7 Binary classification with ELN and explanation

Identical to 2.4, with the only change being the following enhanced label format that also includes an "explanation" field:

```text
    ```json
    {
        "verdict": "correct" | "flawed",
        "erroneous_line_number": "L1", "FA" etc. if "verdict" is "flawed" | "NA" if "verdict" is "correct",
        "explanation": "{A single, short line explaining the error.}"
    }
    ```
```

### 2.8 Ternary classification with ELN and explanation

Identical to 2.5, with the only change being the following enhanced label format that also includes an "explanation" field:

```text
    ```json
    {
        "verdict": "correct" | "conceptual_error" | "computational_error"
        "erroneous_line_number": "L1", "FA" etc. if verdict is not correct | null if verdict is correct
        "explanation": "{short explanation of error}" if verdict is not correct | null if verdict is correct
    }
    ```
```

### 2.9 Final answer + reasoning classification with ELN and explanation

Identical to 2.6, with the only change being the following enhanced label format that also includes an "explanation" field:

```text
    ```json
    {
        "final_answer_verdict": "correct" | "incorrect"
        "reasoning_verdict": "complete" or "missing_step" if final answer is correct | "computational_error" or "conceptual_error" if final answer is incorrect,
        "erroneous_line_number": "L1", "FA" etc. if final_answer_verdict is incorrect | null if verdict is correct,
        "explanation": "{short explanation of error}" if reasoning verdict is not "complete" | null if reasoning verdict is "complete"
    }
    ```
```

# Experiments for product-oriented project

