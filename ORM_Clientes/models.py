from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from .database import Base

# Definición de la clase Cliente que representa la tabla "Clientes"
class Cliente(Base):
    __tablename__ = "Clientes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(index=True)
    apellido: Mapped[str] = mapped_column(String(30),index=True)
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    telefono: Mapped[str] = mapped_column(String(15), index=True)
    pedidos = relationship("Pedido", back_populates="cliente")# relación uno a muchos con la tabla "Pedidos"

# Definición de la clase Pedido que representa la tabla "Pedidos"
class Pedido(Base):
    __tablename__ = "Pedidos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cliente_id: Mapped[int] = mapped_column(Integer, ForeignKey("Clientes.id"))
    descripcion: Mapped[str] = mapped_column(String(100), index=True)
    monto: Mapped[int] = mapped_column(Integer, index=True)
    

# Definición de la clase Ingredientes que representa la tabla "Ingredientes"
class Ingredientes(Base):
    __tablename__ = "Ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50), index=True)
    precio: Mapped[str] = mapped_column(Integer, index=True)
    menus = relationship("Menu", back_populates="ingredientes")# relación uno a muchos con la tabla "Menu"

# Definición de la clase Menu que representa la tabla "Menu"
class Menu(Base):
    __tablename__ = "Menu"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    descripcion: Mapped[str] = mapped_column(String(100), index=True)
    precio: Mapped[int] = mapped_column(Integer, index=True)