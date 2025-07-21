🧠 BERT Sentiment Analyzer (No Fine-Tuning)
This project is a simple yet powerful Sentiment Analyzer that uses a pretrained BERT model from Hugging Face to classify text as Positive or Negative. The user interacts with the system through an intuitive Gradio interface.

🚀 Features:

✅ Uses bert-base-uncased via Hugging Face’s pipeline

✅ Real-time sentiment prediction

✅ Gradio-based interactive UI

✅ No need for local training or fine-tuning

✅ Confidence score with each prediction

🛠️ Tech Stack

Python 3.7+

Hugging Face Transformers

Gradio

PyTorch

📁 Project Structure

sentiment-analyzer/

├── app.py               # Main Gradio app

├── requirements.txt     # Dependencies

└── README.md            # Project description


▶️ How to Run:

Install Dependencies

pip install -r requirements.txt

Run the App

python app.py

Open the Web Interface

Gradio will automatically open a browser tab (usually at http://127.0.0.1:7860) where you can input text and see the predicted sentiment.


Great for demos, learning, and light-weight use — no need for dataset handling or training.
