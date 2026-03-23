-----

# 🚀 Sentiment Analysis Multi-Model Benchmark

A Fullstack Web Application built with **Flask** and **TensorFlow/Keras** to analyze sentiments (Positive, Neutral, Negative) in Vietnamese text. This project serves as a benchmark tool to compare the real-time performance of 13 different Deep Learning architectures.

## ✨ Key Features

  * **Multi-Model Support**: Compare 13 architectures including CNN, LSTM, BiLSTM, GRU, BiGRU, TextCNN, TextRCNN, Transformer, and Attention-based models.
  * **Real-time Benchmarking**: Automatically measures Inference Time (ms) and Confidence Score (%) for every model upon request.
  * **Performance Highlighting**: Automatically identifies and highlights the fastest model in the comparison table.
  * **Vietnamese NLP Pipeline**: Utilizes the `pyvi` library for accurate Vietnamese word segmentation (Tokenization) and preprocessing.
  * **Modern Responsive UI**: Built with Bootstrap 5, featuring smooth loading animations and intuitive result visualization.

## 📂 Project Structure

Before running the application, ensure you have downloaded the trained models and the tokenizer file into the following directory structure:

```text
sentiment_app/
├── models/                     # Directory for trained .keras files
│   ├── model_TextCNN.keras
│   ├── model_BiLSTM.keras
│   └── ... (Other model files)
│   # 📥 Download Models: https://drive.google.com/drive/folders/18b4mdw_wsCtYm0qQ_wp2uosTJ8e4tON5
│
├── static/                     # Static assets (CSS, JS)
│   ├── style.css               # Custom UI styling
│   └── script.js               # API calls & Frontend logic
│
├── templates/                  # HTML templates
│   └── index.html              # Main dashboard
│
├── app.py                      # Flask Backend Server
├── requirements.txt            # Python dependencies
└── tokenizer.pkl               # Word-to-index mapping dictionary
    # 📥 Download Tokenizer: https://drive.google.com/file/d/1TPdQlz56O9NMx5yaJfY0SwmU30SuWVgI
```

## 🛠️ Installation & Setup

1.  **Initialize Virtual Environment (Recommended)**:

    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # MacOS/Linux:
    source venv/bin/activate
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:

    ```bash
    python app.py
    ```

4.  **Access the Web UI**: Open your browser and navigate to `http://127.0.0.1:5000`.

## 📊 Label Mapping

The models predict numerical indices which are mapped to human-readable sentiments:

  * **0**: Negative 😡
  * **1**: Neutral 😐
  * **2**: Positive 😍

-----

**Author:** [hanhdu](https://www.google.com/search?q=https://github.com/hanhdu)

**License:** MIT

-----
