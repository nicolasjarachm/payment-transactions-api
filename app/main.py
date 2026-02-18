from fastapi import FastAPI # Importamos FastAPI para crear la aplicación principal de la API
from app.routes.transactions import router # Importamos el router de transacciones para incluirlo en la aplicación principal

# Creamos la aplicación FastAPI
app = FastAPI()

# Endpoint de prueba para verificar que la API está funcionando
@app.get("/")

def home():
    return {"message": "API funcionando 🚀"}

# Incluimos el router de transacciones en la aplicación principal
app.include_router(router)
