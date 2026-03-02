from fastapi import FastAPI
from src.infra.database.config import criar_db, drop_db
import src.infra.database.models 



criar_db()

app = FastAPI()


@app.get("/teste")
def read_root():
    return {"message": "Hello, World"}

