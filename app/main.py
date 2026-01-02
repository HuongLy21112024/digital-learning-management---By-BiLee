from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import db

app = FastAPI()

# Khai báo thư mục chứa file HTML
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_materials(request: Request):
    # Lấy toàn bộ 1000 học liệu từ MongoDB
    materials = list(db.materials.find())
    return templates.TemplateResponse("index.html", {"request": request, "materials": materials})