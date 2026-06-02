from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from . import service, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return service.get_all_tasks(db)

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return service.get_task_by_id(db, task_id)

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task_data: schemas.TaskCreate, db: Session = Depends(get_db)):
    return service.create_task(db, task_data)

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return service.update_task(db, task_id, task_data)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return service.delete_task(db, task_id)