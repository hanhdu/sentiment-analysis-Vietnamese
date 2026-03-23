-----

# 🎵 YouTube Music Video Sentiment Analyzer

A specialized Fullstack Web Application built with **Flask** and **Deep Learning** to analyze viewer sentiments (Positive, Neutral, Negative) from YouTube music video comments. This tool is designed to help creators and marketers understand audience reactions, from "fan-girling" to "constructive criticism" or even "sarcastic trolls."

## ✨ Industry-Specific Features

  * **13 AI Architectures:** Compare performance across 13 models (CNN, BiLSTM, Transformer, etc.) to see which one best understands complex fan language.
  * **Slang & Sarcasm Ready:** Optimized to detect common Vietnamese music-related slang (e.g., *đỉnh chóp, keo lỳ, gánh còng lưng*).
  * **Real-time Benchmarking:** Measures Inference Time (ms) to show which model is fast enough for large-scale YouTube data scraping.
  * **Context-Aware Analysis:** Specifically tuned for the "Music & Entertainment" domain where emotional expressions are often metaphorical or hyperbolic.

## 📂 Project Structure

Ensure you have downloaded the trained models and the tokenizer file into the following directory structure:

```text
sentiment_app/
├── models/                     # Trained .keras files for music sentiment
│   ├── model_TextCNN.keras
│   ├── model_BiLSTM_Attention.keras
│   └── ... 
│   # 📥 Download Models: https://drive.google.com/drive/folders/18b4mdw_wsCtYm0qQ_wp2uosTJ8e4tON5
│
├── static/                     # Static assets (Custom UI)
│   ├── style.css               
│   └── script.js               
│
├── templates/                  # HTML Templates
│   └── index.html              
│
├── app.py                      # Flask Backend (Sentiment API)
├── requirements.txt            # Dependencies (TensorFlow, Pyvi, Flask)
└── tokenizer.pkl               # Word-index mapping for music vocabulary
    # 📥 Download Tokenizer: https://drive.google.com/file/d/1TPdQlz56O9NMx5yaJfY0SwmU30SuWVgI
```

## 🛠️ Installation & Setup

1.  **Environment Setup**:

    ```bash
    python -m venv venv
    # Activate (Windows):
    venv\Scripts\activate
    ```

2.  **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Dashboard**:

    ```bash
    python app.py
    ```

4.  **Explore**: Navigate to `http://127.0.0.1:5000` and try pasting a "spicy" comment from a trending MV\!

## 📊 Evaluation Metrics (YouTube Context)

| Label | Emoji | Interpretation |
| :--- | :--- | :--- |
| **0 (Negative)** | 😡 | Hate speech, disappointment, or technical complaints. |
| **1 (Neutral)** | 😐 | View counts updates, general questions, or simple mentions. |
| **2 (Positive)** | 😍 | Praising visual/vocal, fan support, or emotional connection. |

-----

**Project:** Sentiment Analysis for Music Industry  
**License:** MIT

-----
