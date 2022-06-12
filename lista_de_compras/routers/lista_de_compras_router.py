from typing import List

from fastapi import APIRouter

from lista_de_compras.models.lista_de_compras_model import ListaDeComprasResponse, ListaDeComprasRequest

router = APIRouter(prefix="/lista_de_compras")


@router.get("/", response_model=List[ListaDeComprasResponse])
def get_lista_compras():
    return [
        ListaDeComprasResponse(
            id=1,
            produto="Café",
            quantidade=2
        ),
        ListaDeComprasResponse(
            id=2,
            produto="Leite",
            quantidade=12
        )
    ]


@router.post("/", response_model=ListaDeComprasResponse, status_code=201)
def post_lista_compras(produto: ListaDeComprasRequest):
    return ListaDeComprasResponse(
        id=1,
        produto=produto.produto,
        quantidade=produto.quantidade
    )
