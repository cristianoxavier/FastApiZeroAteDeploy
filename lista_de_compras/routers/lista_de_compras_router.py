from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.lista_de_compras_model import ListaDeComprasResponse, ProdutoRequest, ListaDeCompras
from shared.dependencies import get_db

router = APIRouter(prefix="/lista-de-compras")


@router.get("/", response_model=List[ListaDeComprasResponse])
def get_lista_compras():
    return [
        ListaDeComprasResponse(
            id=1,
            produto="Café",
            quantidade=2,
            medida="Pacotes"
        ),
        ListaDeComprasResponse(
            id=2,
            produto="Leite",
            quantidade=12,
            medida="Caixas"
        )
    ]


@router.post("/", response_model=ListaDeComprasResponse, status_code=201)
def criar_conta(input: ProdutoRequest,
                db: Session = Depends(get_db)) -> ListaDeComprasResponse:
    item = ListaDeCompras(
        **input.dict()
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item
