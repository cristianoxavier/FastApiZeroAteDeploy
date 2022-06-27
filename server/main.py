import uvicorn
from fastapi import FastAPI
from server.shared.database import engine, Base
from server.lista_de_compras.routers import lista_de_compras_router

app = FastAPI()


app.include_router(lista_de_compras_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
