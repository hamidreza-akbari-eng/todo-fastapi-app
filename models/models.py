from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoResponse(TodoCreate):
    user_id: int
    todo_id: int


class UserResponse(UserCreate):
    user_id: int
    todos: Optional[list[TodoResponse]] = []
