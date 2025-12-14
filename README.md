# FlashCard 📚

FlashCard Master là một ứng dụng học tập sử dụng **Flashcard** kết hợp **Spaced Repetition** giúp người dùng ghi nhớ kiến thức hiệu quả hơn.  
Dự án gồm **Backend (FastAPI)** và **Frontend (HTML/CSS/JS)** tách rời.

---

## 📂 Cấu trúc thư mục

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
