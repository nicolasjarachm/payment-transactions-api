from pydantic import BaseModel, Field # Importamos Field para agregar validaciones a los campos del modelo de datos
from datetime import datetime

#creamos un modelo de datos para las transacciones utilizando Pydantic
class Transaction(BaseModel):
    user: str = Field(min_length=3) # Agregamos una validación para que el nombre de usuario tenga al menos 3 caracteres
    amount: float = Field(gt=0) # Agregamos una validación para que el monto de la transacción sea mayor a 0
    status: str
    created_at: datetime = Field(default_factory=datetime.now)