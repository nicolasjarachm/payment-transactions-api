# Importamos FastAPI para crear la aplicación principal de la API
from fastapi import FastAPI

# Importamos el router de transacciones para incluirlo en la aplicación principal
from app.routes.transactions import router

# Importamos la base de datos y el motor para crear las tablas necesarias
from app.db.database import Base, engine

# Importamos el modelo de transacción para que SQLAlchemy pueda crear la tabla correspondiente en la base de datos
from app.models import db_transaction

# Creamos la aplicación FastAPI
app = FastAPI()


# Crear tablas automáticamente al iniciar la app
Base.metadata.create_all(bind=engine)

# Ruta de prueba para verificar que la API está funcionando correctamente
@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

# Incluimos el router de transacciones en la aplicación principal para que las rutas definidas en el router estén disponibles
app.include_router(router)
