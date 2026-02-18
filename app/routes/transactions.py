from fastapi import APIRouter # Importamos APIRouter para crear rutas específicas para las transacciones
from app.models.transaction import Transaction # Importamos el modelo Transaction para definir la estructura de los datos de las transacciones

# Creamos un router para las transacciones
router = APIRouter()

# Creamos una lista para almacenar las transacciones en memoria (en un entorno real, esto se haría con una base de datos)
transactions = []

# Endpoint para crear una nueva transacción
@router.post("/transactions")
def create_transaction(transaction: Transaction):
    transactions.append(transaction)
    return {"message": "Transacción creada", "data": transaction}

# Endpoint para obtener todas las transacciones
@router.get("/transactions")
def get_transactions():
    return transactions
