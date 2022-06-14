from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_get_lista_de_compras():
    response = client.get('/lista_de_compras/')
    assert response.status_code == 200


def test_post_lista_de_compras():
    produto = {
        "produto": "Banana",
        "quantidade": 1,
        "medida": "Cachos"
    }

    response = client.post("/lista_de_compras/", json=produto)
    assert response.status_code == 201
