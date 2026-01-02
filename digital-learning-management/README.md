# Hệ thống Quản lý Học liệu Số Phân tán
Dự án cuối kỳ môn Hệ thống phân tán.

## Công nghệ sử dụng
- Backend: FastAPI (Python)
- Database: MongoDB Atlas (Cloud NoSQL)
- Thư viện mẫu: Faker (Tạo 1000 dữ liệu)

## Cách cài đặt và khởi chạy
1. Cài đặt thư viện: `pip install -r requirements.txt`
2. Nạp dữ liệu mẫu (1000 bản ghi): `python scripts/seeder.py`
3. Chạy ứng dụng: `uvicorn app.main:app --reload`
4. Truy cập giao diện: `http://127.0.0.1:8000`
