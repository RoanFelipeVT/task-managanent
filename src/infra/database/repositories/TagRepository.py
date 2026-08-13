from sqlalchemy.orm import Session
from src.infra.database.models.tag import Tag

campos_proibidos = {"id", "user_id"} 

class TagRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, tag: Tag) -> Tag:
        tag.user_id = user_id
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        return tag

    def update_field(self, tag_id, user_id, update_data: dict) -> Tag:
        tag = self.db.query(Tag).filter(Tag.user_id == user_id, Tag.id == tag_id).first()
        if not tag:
            raise ValueError("Tag não encontrada")

        for key, value in update_data.itens():
            if key not in campos_proibidos and hasattr(tag, key):
                setattr(tag, key, value)

        self.db.commit()
        self.db.refresh(tag)
        return tag

    def delete(self, tag_id: int, user_id: int) -> None:
        tag = self.db.query(Tag).filter(Tag.user_id == user_id, Tag.id == tag_id).first()
        if not tag:
            raise ValueError("Tag não encontrada")

        self.db.delete(tag)
        self.db.commit()


    