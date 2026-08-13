from sqlalchemy.orm import Session
from src.infra.database.models.task import Task

campos_proibidos = {"id", "user_id"} 

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, task: Task) -> Task:
        task.user_id = user_id
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_field(self, task_id, user_id, update_data: dict) -> Task:
        task = self.db.query(Task).filter(Task.user_id == user_id, Task.id == task_id).first()
        if not task:
            raise ValueError("Tarefa não encontrada")

        for key, value in update_data.itens():
            if key not in campos_proibidos and hasattr(task, key):
                setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    