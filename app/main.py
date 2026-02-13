from fastapi import FastAPI
from pydantic import BaseModel, Field # Importamos Field para agregar validaciones a los campos del modelo de datos
from datetime import datetime

app = FastAPI()

transactions = []

#creamos un modelo de datos para las transacciones utilizando Pydantic
class Transaction(BaseModel):
    user: str = Field(min_length=3) # Agregamos una validación para que el nombre de usuario tenga al menos 3 caracteres
    amount: float = Field(gt=0) # Agregamos una validación para que el monto de la transacción sea mayor a 0
    status: str
    created_at: Field(default_factory=datetime.now)


#endpoints de la API
@app.get("/") #creamos un endpoint para la raíz de la API
def home():
    return {"message": "API funcionando 🚀"}

@app.post("/transactions") #creamos un endpoint para crear transacciones
def create_transaction(transaction: Transaction):
    transactions.append(transaction) # Guardamos la transacción en memoria (en una lista)
    return {
        "message": "Transacción creada",
        "data": transaction
    }

@app.get("/transactions") #creamos un endpoint para obtener todas las transacciones
def get_transactions():
    return transactions
