import os
import time
import re
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from pyvi import ViTokenizer
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# --- CẤU HÌNH ---
MODEL_DIR = 'models'
TOKENIZER_PATH = 'tokenizer.pkl'
MAX_LEN = 100

LABEL_MAPPING = {
    0: 'Tiêu cực',
    1: 'Trung tính',
    2: 'Tích cực'
}

# Biến toàn cục
tokenizer = None
models_dict = {}

def load_resources():
    """Hàm load Tokenizer và toàn bộ Model vào RAM khi khởi động server"""
    global tokenizer, models_dict
    
    # 1. Load Tokenizer
    if os.path.exists(TOKENIZER_PATH):
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer = pickle.load(f)
        print("✅ Đã load Tokenizer thành công!")
    else:
        print("⚠️ Không tìm thấy file tokenizer.pkl!")

    # 2. Load Models
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
        
    model_files = [f for f in os.listdir(MODEL_DIR) if f.endswith(('.h5', '.keras'))]
    if not model_files:
        print("⚠️ Không tìm thấy model nào trong thư mục 'models/'")
        
    for file_name in model_files:
        # Lấy tên rút gọn (ví dụ: model_TextCNN.keras -> TextCNN)
        model_name = file_name.replace('.keras', '').replace('.h5', '').replace('model_', '')
        model_path = os.path.join(MODEL_DIR, file_name)
        try:
            print(f"🔄 Đang load model: {model_name}...")
            models_dict[model_name] = load_model(model_path)
        except Exception as e:
            print(f"❌ Lỗi khi load {model_name}: {e}")
            
    print(f"🚀 Khởi động thành công! Đã load {len(models_dict)} models.")

# Chạy load dữ liệu ngay khi chạy app.py
load_resources()

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^À-ỹA-Za-z0-9\s]', '', text)
    text = ViTokenizer.tokenize(text)
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not tokenizer or not models_dict:
        return jsonify({"error": "Hệ thống chưa load xong tài nguyên."}), 500

    data = request.get_json()
    if not data or 'text' not in data or str(data['text']).strip() == '':
        return jsonify({"error": "Vui lòng nhập văn bản hợp lệ."}), 400

    raw_text = data['text']
    
    # 1. Tiền xử lý
    clean_text = preprocess_text(raw_text)
    seq = tokenizer.texts_to_sequences([clean_text])
    pad = pad_sequences(seq, maxlen=MAX_LEN, padding='post', truncating='post')

    results = []

    # 2. Dự đoán qua từng mô hình
    for model_name, model in models_dict.items():
        # Đo thời gian inference
        start_time = time.time()
        probs = model.predict(pad, verbose=0)[0]
        end_time = time.time()

        predicted_class = int(np.argmax(probs))
        confidence = float(probs[predicted_class])
        time_ms = round((end_time - start_time) * 1000, 2)

        results.append({
            "model": model_name,
            "label": LABEL_MAPPING.get(predicted_class, "Unknown"),
            "confidence": round(confidence * 100, 2),
            "time_ms": time_ms
        })

    # 3. Sắp xếp danh sách trả về theo mức độ tự tin (Confidence) giảm dần
    results = sorted(results, key=lambda x: x['confidence'], reverse=True)

    return jsonify({
        "status": "success",
        "clean_text": clean_text,
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)