from fastapi import FastAPI, HTTPException
from src.infra.database.config import criar_db, drop_db, engine
import src.infra.database.models
from sqlalchemy import inspect




app = FastAPI()


@app.get("/teste")
def read_root():
    return {"message": "Hello, World"}


## Endpoint Utilizado Para Teste de Banco de dados
@app.delete("/database/remove")
def remove_db():

    inspector = inspect(engine)

    if not inspector.get_table_names():
        raise HTTPException(
            status_code=409,
            detail="No tables to remove"
        )

    drop_db()

    return {"message": "Database cleared"}

## Endpoint Utilizado Para Teste de Banco de dados
@app.post("/database/create")
def create_db():

    inspector = inspect(engine)

    if inspector.get_table_names():
        raise HTTPException(
            status_code=409,
            detail="Tables already exist"
        )

    criar_db()

    return {"message": "Database initialized"}

