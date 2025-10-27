from fastapi import FastAPI
from . import models
from .database import engine
from .routers import books

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="📘 Book Management API")

app.include_router(books.router)

@app.get("/")
def home():
    return {"message": "Book Management API ishga tushdi 🚀"}
