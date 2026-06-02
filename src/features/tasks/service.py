from sqlalchemy.orm import Session
from .models import Task
from .schemas import TaskCreate, TaskUpdate

from fastapi import HTTPException

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return task

def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = get_task_by_id(db, task_id)
    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    db.delete(task)
    db.commit()
    return {
        "message": f"Task with id {task_id} deleted successfully!"
    }