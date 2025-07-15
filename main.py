from fastapi import FastAPI

from routers.todo_routers import router as todo_router
from routers.user_routers import router as user_router

app = FastAPI()


app.include_router(user_router)
app.include_router(todo_router)
