---
title: Math Solution Classifier
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Math Solution Classifier

This application classifies math solutions into three categories:
- **Correct**: Solution is mathematically sound
- **Conceptually Flawed**: Wrong approach or understanding  
- **Computationally Flawed**: Right approach, calculation errors

## Usage

1. Enter a math question
2. Enter the proposed solution
3. Click "Classify Solution"
4. Get instant feedback on the solution quality

Built with Gradio and your custom trained model.

# requirements.txt
gradio==4.44.0
torch==2.1.0
transformers==4.35.0
peft==0.7.1
accelerate==0.25.0