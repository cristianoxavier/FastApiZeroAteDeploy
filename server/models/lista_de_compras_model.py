from pydantic import BaseModel, Field
from sqlalchemy import Integer, Column, String
from server.shared.database import Base


class ListaDeCompras(Base):
    __tablename__ = 'tb_lista_de_compras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(30))
    quantidade = Column(Integer)
    medida = Column(String(30))


class ListaDeComprasResponse(BaseModel):
    id: int
    produto: str
    quantidade: int
    medida: str

    class Config:
        orm_mode = True


class ProdutoRequest(BaseModel):
    produto: str = Field(min_length=3, max_length=20)
    quantidade: int = Field()
    medida: str = Field()
