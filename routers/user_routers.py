from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal, Users
from models.models import UserCreate, UserResponse


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/user/create_user", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = Users(
        name=user.name,
        email=user.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserResponse])
async def read_all_users_and_todos(db: Session = Depends(get_db)):
    db_users = db.query(Users).all()
    if db_users is None:
        raise HTTPException(status_code=404, detail="there is no user in th edatabase!")
    return db_users


@router.get("/user/{user_id}", response_model=UserResponse)
async def read_specefic_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found in databas!")
    return user


@router.put("/user/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found in databas!")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/user/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found in databas!")
    db.delete(db_user)
    db.commit()
    return {"message": f"user with id:{user_id} deleted successfully."}
