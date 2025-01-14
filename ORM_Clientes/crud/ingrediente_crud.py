from sqlalchemy.orm import Session
from models import Ingrediente
from .crud_base import CRUDBase
from factory import IngredienteFactory

class IngredienteCRUD(CRUDBase):
    def __init__(self):
        self.factory = IngredienteFactory()
    
    def leer(self, db: Session):
        return db.query(Ingrediente).all()  # Retorna todos los ingredientes
    
    def agregar(self, db: Session, nombre: str, stock: int):
        ingrediente_existente = db.query(Ingrediente).filter(Ingrediente.nombre == nombre).first()
        if ingrediente_existente:
            ingrediente_existente.stock += stock
            db.commit()
            db.refresh(ingrediente_existente)
        else:
            ingrediente = self.factory.crear_objeto()
            ingrediente.nombre = nombre
            ingrediente.stock = stock
            db.add(ingrediente)
            db.commit()
            db.refresh(ingrediente)
            return ingrediente
    
    def modificar(self, db: Session, id: int, nombre: str = None, stock: int = None):
        ingrediente = db.query(Ingrediente).get(id)
        if ingrediente:
            if nombre:
                ingrediente.nombre = nombre
            if stock is not None:
                ingrediente.stock = stock
            db.commit()
            db.refresh(ingrediente)
            return ingrediente
        else:
            print("Ingrediente no encontrado")
            return None
    
    def borrar(self, db: Session, id: int):
        ingrediente = db.query(Ingrediente).get(id)
        if ingrediente:
            db.delete(ingrediente)
            db.commit()
        return ingrediente