import uvicorn
from fastapi import FastAPI
from shared.database import engine, Base
from lista_de_compras.routers import lista_de_compras_router


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(lista_de_compras_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
