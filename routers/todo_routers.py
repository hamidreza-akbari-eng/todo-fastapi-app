from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal, Todos
from models.models import TodoCreate, TodoResponse


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/todo/{user_id}", response_model=TodoResponse)
async def create_todo(user_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todos(title=todo.title, description=todo.description, user_id=user_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/todo/{todo_id}", response_model=TodoResponse)
async def read_specefic_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todos).filter(Todos.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"there is not todo with id:{todo_id} !"
        )
    return db_todo


@router.get("/todos", response_model=list[TodoResponse])
async def read_all_todos(db: Session = Depends(get_db)):
    db_todos = db.query(Todos).all()
    if db_todos is None:
        raise HTTPException(status_code=404, detail="there is no todo in the database!")
    return db_todos


@router.put("/todo/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todos).filter(Todos.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"there is no todo with id:{todo_id} !"
        )
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todos).filter(Todos.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"there is no todo with id:{todo_id} !"
        )
    db.delete(db_todo)
    db.commit()
    return {"message": f"todo with ID:{todo_id} deleted_succesfully!"}
