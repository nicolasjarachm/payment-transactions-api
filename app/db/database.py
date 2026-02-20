#crea sql lite database y session para interactuar con la base de datos
from sqlalchemy import create_engine
# Declarative base para definir modelos de datos
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./payments.db"

# Crear el motor de la base de datos con la URL especificada y configuraciones necesarias para SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

