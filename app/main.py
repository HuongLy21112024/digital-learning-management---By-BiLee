from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import db
import json
from bson import json_util

app = FastAPI()

# Khai báo thư mục chứa file HTML (Dùng "app/templates" vì thư mục app đã ở ngoài cùng)
templates = Jinja2Templates(directory="app/templates")

# 1. API để hiển thị trang chủ
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. API để trả về dữ liệu JSON cho bảng (Sửa lỗi 404 này)
@app.get("/materials")
async def get_materials_data():
    # Lấy dữ liệu từ MongoDB
    materials = list(db.materials.find().limit(1000))
    # Chuyển đổi định dạng MongoDB sang JSON chuẩn
    return json.loads(json_util.dumps(materials))
