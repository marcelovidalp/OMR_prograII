from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

# Tabla de asociación para la relación muchos a muchos entre Pedido y Ingredientes
pedido_ingredientes = Table(
    'pedido_ingredientes', Base.metadata,
    Column('pedido_id', Integer, ForeignKey('Pedidos.id'), primary_key=True),
    Column('ingrediente_id', Integer, ForeignKey('Ingredientes.id'), primary_key=True)
)

# Definición de la clase Cliente que representa la tabla "Clientes"
class Cliente(Base):
    __tablename__ = "Clientes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)

    pedidos = relationship("Pedido", back_populates="cliente")  # relación uno a muchos con la tabla "Pedidos"

# Definición de la clase Pedido que representa la tabla "Pedidos"
class Pedido(Base):
    __tablename__ = "Pedidos"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cliente_id: Mapped[int] = mapped_column(Integer, ForeignKey("Clientes.id"))
    descripcion: Mapped[str] = mapped_column(String(100), index=True)
    monto: Mapped[int] = mapped_column(Integer, index=True)

    cliente = relationship("Cliente", back_populates="pedidos")  # relación inversa con la tabla "Clientes"
    ingredientes = relationship("Ingredientes", secondary=pedido_ingredientes, back_populates="pedidos")  # relación muchos a muchos con la tabla "Ingredientes"

# Definición de la clase Ingredientes que representa la tabla "Ingredientes"
class Ingredientes(Base):
    __tablename__ = "Ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    precio: Mapped[int] = mapped_column(Integer, index=True)

    pedidos = relationship("Pedido", secondary=pedido_ingredientes, back_populates="ingredientes")  # relación muchos a muchos con la tabla "Pedidos"

# Definición de la clase Menu que representa la tabla "Menu"
class Menu(Base):
    __tablename__ = "Menu"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    descripcion: Mapped[str] = mapped_column(String(100), index=True)
    precio: Mapped[int] = mapped_column(Integer, index=True)
