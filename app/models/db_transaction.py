from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base

class DBTransaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    amount = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
