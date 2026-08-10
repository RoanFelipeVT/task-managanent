from datetime import date
from src.infra.database.repositories.UserRepository import UserRepository
from src.infra.database.models.user import User
from typing import Any

def test_create_user(db_session):

    repo = UserRepository(db_session)

    user = User(
        email="test@email.com",
        name="teste",
        password="123",
        cellphone="123456789"
        )

    result = repo.create(user)

    assert result.id is not None
    assert result.email == "test@email.com" 
    assert result.password != "abc" 


def test_update_user(db_session):

    repo = UserRepository(db_session)


    user = User(
        email="test@email.com",
        name="teste",
        password="123",
        cellphone="123456789"
    )

    user = repo.create(user)

    user_updated_field = {
        "name": "Róger",
        "email": "update@gmail.com",
        "password": "updated",
        "cellphone": "987654321"
    }

    updated_user = repo.update_field(user.id, user_updated_field)

    assert updated_user.name == "Róger"
    assert updated_user.email == "update@gmail.com"
    assert updated_user.password == "updated"
    assert updated_user.cellphone == "987654321"
    

   