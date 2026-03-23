# 🚀 Hướng Dẫn Chạy Ứng Dụng Sentiment Analysis

Đây là ứng dụng Web Fullstack (Flask + Keras + Vanilla JS) giúp đánh giá và so sánh hiệu năng của nhiều mô hình Deep Learning khác nhau trong bài toán Phân tích cảm xúc văn bản Tiếng Việt.

## ⚙️ 1. Cài đặt môi trường (Khuyên dùng)

Để tránh xung đột thư viện với các dự án khác trên máy của bạn, hãy tạo một môi trường ảo (Virtual Environment).

**Mở Terminal (hoặc Command Prompt) tại thư mục dự án và chạy các lệnh sau:**

**Dành cho Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Dành cho MacOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

## 📦 2. Cài đặt thư viện

Sau khi kích hoạt môi trường ảo, hãy cài đặt các thư viện cần thiết đã được liệt kê trong file `requirements.txt`:

```bash
pip install -r requirements.txt
```

*(Quá trình này có thể mất vài phút tùy thuộc vào tốc độ mạng, đặc biệt là khi tải TensorFlow).*

## 🏃‍♂️ 3. Khởi động Server

Chạy lệnh sau để khởi động Backend Flask:

```bash
python app.py
```

Khi Terminal hiển thị dòng chữ:

```text
🚀 Khởi động thành công! Đã load các models.
* Running on http://127.0.0.1:5000
```

Nghĩa là hệ thống đã sẵn sàng\!

## 🌐 4. Sử dụng ứng dụng

1.  Mở trình duyệt web (Chrome, Edge, Safari...).
2.  Truy cập vào địa chỉ: [http://127.0.0.1:5000](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:5000)
3.  Nhập một câu bình luận Tiếng Việt vào ô trống và bấm **"Phân Tích Ngay"**.
4.  Chờ ứng dụng chạy qua tất cả các mô hình và hiển thị bảng xếp hạng tốc độ & độ tự tin.

-----

### ⚠️ Một số lỗi thường gặp & Cách xử lý:

  * **Lỗi `FileNotFoundError: [Errno 2] No such file or directory: 'tokenizer.pkl'`**: Đảm bảo file `tokenizer.pkl` nằm cùng thư mục với file `app.py`.
  * **Mở web lên dự đoán bị báo lỗi 500**: Có thể thư mục `models/` của bạn đang trống. Hãy kiểm tra lại xem đã bỏ các file `.keras` vào chưa.
  * **Lỗi tràn RAM máy tính**: Nếu máy tính của bạn có RAM yếu (dưới 8GB), việc load cùng lúc nhiều mô hình Deep Learning có thể gây đứng máy. **Mẹo:** Hãy giữ lại 3-5 mô hình tốt nhất trong thư mục `models/` và xóa/di chuyển các mô hình còn lại đi chỗ khác.