from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

# Definición de la clase Cliente que representa la tabla "Clientes"
class Cliente(Base):
    __tablename__ = "Clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, index=True)

# Definición de la clase Pedido que representa la tabla "Pedidos"
class Pedido(Base):
    __tablename__ = "Pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Clientes.id"), index=True)
    descripcion = Column(String, index=True)
    monto = Column(Integer, index=True)

# Definición de la clase Ingredientes que representa la tabla "Ingredientes"
class Ingredientes(Base):
    __tablename__ = "Ingredientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Integer, index=True)

# Definición de la clase Menu que representa la tabla "Menu"
class Menu(Base):
    __tablename__ = "Menu"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    precio = Column(Integer, index=True)