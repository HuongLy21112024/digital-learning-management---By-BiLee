from pydantic import BaseModel

class Material(BaseModel):
    title: str
    faculty: str
    author: str
    description: str
    views: int