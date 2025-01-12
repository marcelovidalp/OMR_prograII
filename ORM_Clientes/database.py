from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos
url = "sqlite:///mi_base_de_datos.db"

# Crear el motor de la base de datos
engine = create_engine(url, echo=True)

# Crear una clase base para los modelos
Base = declarative_base()

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia de la sesión de la base de datos
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
