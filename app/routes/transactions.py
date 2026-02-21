# importamos api router y Depends para manejar las dependencias en las rutas
from fastapi import APIRouter, Depends

# importamos Session para manejar las sesiones de la base de datos
from sqlalchemy.orm import Session

# importamos get_db para obtener la sesión de la base de datos
from app.db.database import get_db

# importamos el modelo de base de datos
from app.models.db_transaction import DBTransaction

# importamos los esquemas Pydantic
from app.models.transaction import TransactionCreate, TransactionResponse

# Creamos un router
router = APIRouter()

# POST /transactions
@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):

    db_transaction = DBTransaction(
        user=transaction.user,
        amount=transaction.amount,
        status=transaction.status
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


# GET /transactions
@router.get("/transactions", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):

    return db.query(DBTransaction).all()


# GET /transactions/{id}

from fastapi import HTTPException


@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_id(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(DBTransaction).filter(
        DBTransaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction

#Que hace GET /transactions/{id}?
#Recibe el ID desde una URL
#Busca en la base de datos
#Si no existe, devuelve un error 404
#Si existe, devuelve la transacción encontrada (el objeto DBTransaction)


# DELETE /transactions/{id}

from fastapi import HTTPException


@router.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(DBTransaction).filter(
        DBTransaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}

#que hace DELETE /transactions/{id}?
#Busca por ID
#Si no existe devuelve error 404
#Si existe, borra la transacción y devuelve un mensaje de éxito
#Hace commit para guardar los cambios en la base de datos
#Devuelve un mensaje de exito
