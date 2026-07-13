from datetime import date
from src.infra.database.repositories.UserRepository import UserRepository
from src.infra.database.models.user import User
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