from fastapi import FastAPI
from pydantic import BaseModel

class Transaction(BaseModel): # Definimos un modelo de datos para las transacciones
    user: str
    amount: float
    status: str

app = FastAPI()

transactions = []

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
