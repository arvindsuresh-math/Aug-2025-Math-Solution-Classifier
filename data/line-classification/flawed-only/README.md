# Flawed-Only Line Classification Dataset (Preprocessed)

Created on: 2025-07-30 10:52:37
Random seed: 42
Strategy: **Flawed-Only with Comprehensive Preprocessing**

## Overview

This dataset addresses class imbalance by using **only flawed samples** for line-level error detection, with comprehensive preprocessing applied to fix tokenization issues and standardize input format.

## Key Improvements

### 1. Class Balance
- **Original approach**: ~85-90% zeros (severe imbalance, ratio ~5-6:1)
- **Flawed-only approach**: ~77.5% zeros (better balance, ratio ~3.4:1)

### 2. Preprocessing Applied
- **Line separation**: Replaced newlines with special token `<|LINE_SEP|>` for reliable tokenization
- **Unicode sanitization**: Converted problematic Unicode characters to ASCII equivalents
- **User prompt formatting**: Combined question + solution into standardized format
- **Text cleaning**: Removed comma separators from numbers

## Dataset Structure

- **Total samples**: 3,487 (all flawed)
- **Unique problems**: 3,487
- **Strategy**: Balanced conceptual + computational errors with preprocessing

### Composition
- **Conceptual errors**: 1881 samples
- **Computational errors**: 1606 samples
- **Correct solutions**: 0 samples (removed to eliminate imbalance)

### Class Balance Analysis
- **Total line positions**: 15,477
- **Error lines (label=1)**: 3,487 (22.5%)
- **Correct lines (label=0)**: 11,990 (77.5%)
- **Imbalance ratio**: 3.4:1

## Column Descriptions

- `text`: Complete user prompt with system instruction + problem + preprocessed solution
- `correct_answer`: Original GSM8K correct answer for reference
- `line_labels`: One-hot encoded labels `[0,0,1,0,...]` indicating error line
- `error_type`: 'conceptual_error' or 'computational_error'
- `index`: Original GSM8K problem index
- `tier`: Problem difficulty tier (tier1-tier4)
- `source`: 'manual' or 'programmatic'

## Usage Example

```python
import pandas as pd
import ast

# Load dataset
df = pd.read_csv('flawed_only_line_classification_dataset.csv')

# Parse line_labels from string representation
df['line_labels'] = df['line_labels'].apply(ast.literal_eval)

# Example: Check a sample with error
sample = df.iloc[0]
print("User prompt:")
print(sample['text'])
print(f"\nError type: {sample['error_type']}")
print(f"Error line position: {sample['line_labels'].index(1)}")
```

## Training Considerations

- **Tokenization**: Preprocessing ensures reliable newline token detection
- **Loss function**: Standard cross-entropy works well (no complex weighting needed)
- **Data collator**: Custom collator for variable-length `line_labels`
- **Evaluation**: Line-level accuracy, precision, recall, F1
- **Much more stable training** than severely imbalanced dataset