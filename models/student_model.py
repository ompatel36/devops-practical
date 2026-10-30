from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    id: int = 0
    name: str
    course: str
    marks: int