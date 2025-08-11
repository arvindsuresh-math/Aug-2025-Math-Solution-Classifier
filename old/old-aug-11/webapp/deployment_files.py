# requirements.txt
fastapi==0.104.1
uvicorn==0.24.0
torch==2.1.0
transformers==4.35.0
python-multipart==0.0.6
pydantic==2.5.0

# README.md for your Hugging Face Space
---
title: Math Solution Classifier
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.7.1
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

Built with FastAPI and your custom trained model.

# Dockerfile (optional, for other hosting platforms)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]