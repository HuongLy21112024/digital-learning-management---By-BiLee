from pymongo import MongoClient
import sys

# Đã cập nhật mật khẩu: JXrykOPcCSvp47Zh (chữ c thường và S hoa)
uri = "mongodb+srv://huongvip2442_db_user:JXrykOPcCSvp47Zh@learning-management-clu.jnq09e8.mongodb.net/?retryWrites=true&w=majority&appName=Learning-Management-Cluster"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    # Kiểm tra kết nối
    client.admin.command('ping')
    db = client['learning_management']
    print("✅ KẾT NỐI CLOUD THÀNH CÔNG!")
except Exception as e:
    print(f"❌ THẤT BẠI: Lỗi xác thực hoặc mạng.")
    print(f"Chi tiết lỗi: {e}")
    sys.exit(1)