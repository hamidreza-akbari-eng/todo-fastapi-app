from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    name: Mapped[str]
    email: Mapped[str]
    user_id: Mapped[int] = mapped_column(primary_key=True)

    todos: Mapped[list["Todos"]] = relationship("Todos", back_populates="user")


class Todos(Base):
    __tablename__ = "todos"
    todo_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    user: Mapped["Users"] = relationship("Users", back_populates="todos")


DATABASE_URL = "sqlite:///./todoapp_db.db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
