from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.main import app
from server.shared.database import Base
from server.shared.dependencies import get_db

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_get_lista_de_compras():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    produto = {
        "produto": "Banana",
        "quantidade": 1,
        "medida": "Cachos"
    }

    response = client.post("/lista-de-compras/", json=produto)

    response = client.get('/lista-de-compras/')
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "produto": "Banana", "quantidade": 1, "medida": "Cachos"}
    ]


def test_post_lista_de_compras():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    produto = {
        "produto": "Banana",
        "quantidade": 1,
        "medida": "Cachos"
    }

    response = client.post("/lista-de-compras/", json=produto)
    assert response.status_code == 201


def test_deve_retornar_erro_quando_exceder_o_nome_produto():
    produto = {
        "produto": "Bananananananananaasndjasndujanasdqwdasdqwdqsdq",
        "quantidade": 1,
        "medida": "Bananananananananaasndjasndujanasdqwdasdqwdqsdq"
    }
    response = client.post("/lista-de-compras/", json=produto)
    assert response.status_code == 422