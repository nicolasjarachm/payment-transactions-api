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

# importamos el modelo para la paginación de transacciones
from app.models.transaction import PaginatedTransactions


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
#Endpoint para obtener una lista de transacciones con paginación

from fastapi import Query
import math

@router.get("/transactions", response_model=PaginatedTransactions)
def get_transactions(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    status: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(DBTransaction)

    if status:
        query = query.filter(DBTransaction.status == status)

    total = query.count()

    offset = (page - 1) * limit

    transactions = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

    total_pages = math.ceil(total / limit) if total > 0 else 1

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "data": transactions
    }

#Que hace GET /transactions?
#Recibe parámetros de paginación (page y limit) desde la URL
#Calcula el offset para la consulta a la base de datos
#Realiza una consulta a la base de datos
#Devuelve una lista de transacciones según la página y el límite especificados



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

# PUT /transactions/{id}
from app.models.transaction import TransactionUpdate


@router.patch("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction(
    transaction_id: int,
    transaction_update: TransactionUpdate,
    db: Session = Depends(get_db)
):
    transaction = db.query(DBTransaction).filter(
        DBTransaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    update_data = transaction_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)

    return transaction

#Permite
#exclude_unset=True, solo actualiza lo que enviamos
#setattr para actualizar los campos dinámicamente
#commit para guardar los cambios
#refresh para obtener la transacción actualizada de la base de datos
#devuelve objeto actualizado

