from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_lista_de_compras():
    response = client.get('/lista_de_compras/')
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'produto': 'Café', 'quantidade': 2},
        {'id': 2, 'produto': 'Leite', 'quantidade': 12}
    ]


def test_post_lista_de_compras():
    produto = {
      "produto": "Banana",
      "quantidade": 1
    }
    novo_produto = produto.copy()
    novo_produto["id"] = 1

    response = client.post("/lista_de_compras/", json=produto)
    assert response.status_code == 201
    assert response.json() == novo_produto