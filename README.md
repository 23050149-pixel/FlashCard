FlashCard Study App

Nhóm thực hiện:
23050188 – Lab

📖 Giới thiệu đề tài

FlashCard Study App là ứng dụng Web hỗ trợ học tập bằng flashcard, được xây dựng làm tiểu luận môn Phát triển ứng dụng mã nguồn mở.
Ứng dụng cho phép người dùng tạo flashcard, học tập theo phương pháp Spaced Repetition và theo dõi tiến trình học tập.

Hệ thống được xây dựng theo mô hình Client – Server, bao gồm backend cung cấp RESTful API và frontend giao diện web.

🎯 Mục tiêu

Áp dụng kiến thức môn học vào thực tế

Xây dựng RESTful API bằng FastAPI

Thiết kế hệ thống Client–Server

Hỗ trợ học tập và ghi nhớ hiệu quả bằng flashcard

✨ Chức năng chính

Đăng ký / đăng nhập người dùng

Quản lý flashcard (thêm, sửa, xoá)

Học flashcard theo Spaced Repetition

Theo dõi tiến trình học

Giao diện web tương tác

🧰 Công nghệ sử dụng

Backend: Python, FastAPI

Frontend: HTML, CSS, JavaScript

Cơ sở dữ liệu: SQLite
🖥️ Cấu trúc thư mục
```bash
FLASHCARD-MASTER/
│
├── backend/                # Backend FastAPI
│   ├── __pycache__/
│   ├── crud.py             # Xử lý CRUD cho database
│   ├── database.py         # Kết nối CSDL
│   ├── main.py             # Entry point chạy FastAPI
│   ├── models.py           # Định nghĩa ORM models
│   ├── schemas.py          # Pydantic schemas
│   ├── security.py         # Xác thực, bảo mật (hash password, token)
│   ├── spaced_repetition.py# Thuật toán lặp lại ngắt quãng
│   └── requirements.txt    # Danh sách thư viện Python
│
├── frontend/               # Giao diện người dùng
│   ├── index.html          # Trang chủ
│   ├── login.html          # Đăng nhập
│   ├── register.html       # Đăng ký
│   ├── profile.html        # Thông tin cá nhân
│   ├── progress.html       # Thống kê tiến độ học
│   ├── daily_goal.html     # Mục tiêu học tập hằng ngày
│   ├── flashcard_detail.html # Chi tiết flashcard
│   ├── admin.html          # Trang quản trị
│   └── admin_user.html     # Quản lý người dùng (admin)
│
└── README.md
```


▶️ Hướng dẫn chạy dự án (Windows)
Yêu cầu

Windows 10/11

Python 3.9+

VS Code + Live Server

Bước 1. Clone mã nguồn
git clone https://github.com/<repo>/FlashCard-master.git
cd FlashCard-master

Bước 2. Chạy Backend
python -m venv venv
venv\Scripts\activate
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend chạy tại:
👉 http://127.0.0.1:8000

👉 Swagger UI: http://127.0.0.1:8000/docs

Bước 3. Chạy Frontend

Mở thư mục frontend/ bằng VS Code

Chuột phải index.html → Open with Live Server

Frontend chạy tại:
👉 http://127.0.0.1:5500
