import sys
import os
# Thêm đường dẫn để script hiểu được thư mục app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import db
from faker import Faker
import random

fake = Faker()
faculties = ["CNTT", "Kinh tế", "Ngoại ngữ", "Cơ khí"]

def run_seeder():
    print("⏳ Đang tạo 1000 học liệu mẫu...")
    materials = []
    for _ in range(1000):
        materials.append({
            "title": fake.sentence(nb_words=5),
            "faculty": random.choice(faculties),
            "author": fake.name(),
            "description": fake.text(max_nb_chars=150),
            "views": random.randint(0, 5000)
        })
    
    db.materials.delete_many({}) # Xóa cũ
    db.materials.insert_many(materials) # Chèn 1000 cái mới
    print("✅ Đã nạp 1000 dữ liệu thành công lên MongoDB Atlas!")

if __name__ == "__main__":
    run_seeder()