#Importamos Field para agregar validaciones a los campos del modelo de datos
from pydantic import BaseModel, Field
#Importamos datetime para agregar un campo de fecha y hora a las transacciones
from datetime import datetime

#creamos un modelo de datos para las transacciones utilizando Pydantic
class TransactionCreate(BaseModel):
    user: str = Field(min_length=3)
    amount: float = Field(gt=0)
    status: str

class TransactionResponse(TransactionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

#Esto sirve para
#Validar lo que llega al POST
#Convertir objetos DB -> JSON para las respuestas del API