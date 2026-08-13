from sqlalchemy.orm import Session
from src.infra.database.models.user import User


campos_proibidos = {"id"}

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_field(self, user_id, update_data: dict) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("Usuário não encontrado")

        for key, value in update_data.items():
            if key not in campos_proibidos and hasattr(user, key):
                setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    
