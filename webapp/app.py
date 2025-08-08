# app.py - Gradio version (much simpler for HF Spaces)

import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging
import spaces

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables for model and tokenizer
model = None
tokenizer = None
label_mapping = {0: "✅ Correct", 1: "🤔 Conceptually Flawed", 2: "🔢 Computationally Flawed"}

def load_model():
    """Load your trained model here"""
    global model, tokenizer
    
    try:
        # Replace these with your actual model path/name
        # Option 1: Load from local files
        # model = AutoModelForSequenceClassification.from_pretrained("./your_model_directory")
        # tokenizer = AutoTokenizer.from_pretrained("./your_model_directory")
        
        # Option 2: Load from Hugging Face Hub (if you upload your model there)
        # model = AutoModelForSequenceClassification.from_pretrained("your-username/your-model-name")
        # tokenizer = AutoTokenizer.from_pretrained("your-username/your-model-name")
        
        # For now, we'll use a placeholder - replace this with your actual model loading
        logger.warning("Using placeholder model loading - replace with your actual model!")
        
        # Placeholder model loading (replace this!)
        model_name = "distilbert-base-uncased"  # Replace with your model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name, 
            num_labels=3,
            ignore_mismatched_sizes=True
        )
        
        logger.info("Model loaded successfully")
        return "Model loaded successfully!"
        
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return f"Error loading model: {e}"

@spaces.GPU
def classify_solution(question: str, solution: str):
    """
    Classify the math solution
    Returns: (classification_label, confidence_score, explanation)
    """
    if not question.strip() or not solution.strip():
        return "Please fill in both fields", 0.0, ""
    
    if not model or not tokenizer:
        return "Model not loaded", 0.0, ""
    
    try:
        # Combine question and solution for input
        text_input = f"Question: {question}\nSolution: {solution}"
        
        # Tokenize input
        inputs = tokenizer(
            text_input,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )
        
        # Get model prediction
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
            predicted_class = torch.argmax(predictions, dim=-1).item()
            confidence = predictions[0][predicted_class].item()
        
        classification = label_mapping[predicted_class]
        
        # Create explanation based on classification
        explanations = {
            0: "The mathematical approach and calculations are both sound.",
            1: "The approach or understanding has fundamental issues.",
            2: "The approach is correct, but there are calculation errors."
        }
        
        explanation = explanations[predicted_class]
        
        return classification, f"{confidence:.2%}", explanation
        
    except Exception as e:
        logger.error(f"Error during classification: {e}")
        return f"Classification error: {str(e)}", "0%", ""

# Load model on startup
load_model()

# Create Gradio interface
with gr.Blocks(title="Math Solution Classifier", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🧮 Math Solution Classifier")
    gr.Markdown("Classify math solutions as correct, conceptually flawed, or computationally flawed.")
    
    with gr.Row():
        with gr.Column():
            question_input = gr.Textbox(
                label="Math Question",
                placeholder="e.g., Solve for x: 2x + 5 = 13",
                lines=3
            )
            
            solution_input = gr.Textbox(
                label="Proposed Solution", 
                placeholder="e.g., 2x + 5 = 13\n2x = 13 - 5\n2x = 8\nx = 4",
                lines=5
            )
            
            classify_btn = gr.Button("Classify Solution", variant="primary")
        
        with gr.Column():
            classification_output = gr.Textbox(label="Classification", interactive=False)
            confidence_output = gr.Textbox(label="Confidence", interactive=False)
            explanation_output = gr.Textbox(label="Explanation", interactive=False, lines=3)
    
    # Examples
    gr.Examples(
        examples=[
            [
                "Solve for x: 2x + 5 = 13",
                "2x + 5 = 13\n2x = 13 - 5\n2x = 8\nx = 4"
            ],
            [
                "John has three apples and Mary has seven, how many apples do they have together?", 
                "They have 7 + 3 = 11 apples."  # This should be computationally flawed
            ],
            [
                "What is 15% of 200?",
                "15% = 15/100 = 0.15\n0.15 × 200 = 30"
            ]
        ],
        inputs=[question_input, solution_input]
    )
    
    classify_btn.click(
        fn=classify_solution,
        inputs=[question_input, solution_input],
        outputs=[classification_output, confidence_output, explanation_output]
    )

if __name__ == "__main__":
    app.launch()