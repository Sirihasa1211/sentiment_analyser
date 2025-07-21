from transformers import pipeline
import gradio as gr

# Load sentiment analysis pipeline using BERT
sentiment_pipeline = pipeline("sentiment-analysis")

# Define prediction function
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = round(result['score'] * 100, 2)
    return f"Sentiment: {label} ({score}%)"

# Gradio Interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analyzer with BERT",
    description="This app uses BERT (via Hugging Face Transformers) to classify sentiment as Positive or Negative."
)

iface.launch()
