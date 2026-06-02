from fastapi import FastAPI

from src.features.tasks.router import router as tasks_router

app = FastAPI(
    title="To-Do List API",
    description="A simple API for managing tasks in a to-do list application.",
)

app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"Message": "Bienvenido a la API de To-Do List!"}
