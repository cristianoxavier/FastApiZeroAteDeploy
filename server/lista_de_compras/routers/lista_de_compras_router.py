from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.models.lista_de_compras_model import ListaDeComprasResponse, ProdutoRequest, ListaDeCompras
from server.shared.dependencies import get_db

router = APIRouter(prefix="/lista-de-compras")


@router.get("/", response_model=List[ListaDeComprasResponse])
def get_lista_compras(db: Session = Depends(get_db))->List[ListaDeComprasResponse]:
    return db.query(ListaDeCompras).all()


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
