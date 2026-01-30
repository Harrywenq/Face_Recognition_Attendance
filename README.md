# Hệ thống chấm công bằng nhận diện khuôn mặt (Face Recognition Attendance System)

## 📌 Giới thiệu
Đây là project cá nhân xây dựng **hệ thống chấm công bằng nhận diện khuôn mặt**, sử dụng camera realtime.  
Hệ thống có tích hợp **liveness detection (chớp mắt)** nhằm hạn chế gian lận bằng ảnh hoặc video.

---

## ⚙️ Công nghệ sử dụng
- **Python 3.9**
- **OpenCV**
- **MediaPipe** (Face Mesh – liveness detection)
- **LBPH Face Recognizer**
- **SQLite** (lưu dữ liệu chấm công)

---

## 🧠 Chức năng chính
- Mở camera realtime
- Phát hiện chớp mắt để xác thực người thật (liveness detection)
- Nhận diện khuôn mặt bằng thuật toán LBPH
- Ghi nhận thời gian chấm công vào database
- Hiển thị kết quả trực tiếp trên màn hình

---

## 📂 Cấu trúc thư mục
face-recognition-attendance-system/
│
├── main.py # File chạy chính
├── blink_liveness.py # Liveness detection (chớp mắt)
├── face_recognition_lbph.py # Nhận diện khuôn mặt
├── attendance.py # Lưu dữ liệu chấm công
│
└── data/
├── faces/ # Dataset khuôn mặt
│ └── employee01/
│   ├── 1.jpg
│   ├── 2.jpg
└── attendance.db # Database SQLite


---

## ▶️ Cách cài đặt

### 1️⃣ Cài thư viện
```bash
pip install opencv-python mediapipe numpy
2️⃣ Chuẩn bị dữ liệu khuôn mặt
Tạo thư mục trong data/faces/ theo mã nhân viên (employee01)

Mỗi người nên có 2–5 ảnh, chụp rõ mặt, đủ sáng

▶️ Cách chạy chương trình
python main.py

Luồng hoạt động:
1. Camera được mở

2. Người dùng chớp mắt để xác thực liveness

3. Hệ thống nhận diện khuôn mặt

4. Nếu hợp lệ → lưu thời gian chấm công vào database

🧪 Kết quả
Hiển thị trạng thái trực tiếp trên camera

In log chấm công trên terminal

Dữ liệu được lưu trong file attendance.db