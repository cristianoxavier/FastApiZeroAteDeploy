from pydantic import BaseModel


class ListaDeComprasResponse(BaseModel):
    id: int
    produto: str
    quantidade: int


class ListaDeComprasRequest(BaseModel):
    produto: str
    quantidade: int