from sqlalchemy.orm import Session
from models import Ingrediente
from .crud_base import CRUDBase

class IngredienteCRUD(CRUDBase):
    def ver(self, db: Session):
        return db.query(Ingrediente).all()
    
    def agregar(self, db: Session, nombre: str, stock: int):
        ingrediente = Ingrediente(nombre=nombre, stock=stock)
        db.add(ingrediente)
        db.commit()
        db.refresh(ingrediente)
        return ingrediente
    
    def modificar(self, db: Session, id: int, nombre: str = None, stock: int = None):
        ingrediente = db.query(Ingrediente).get(id)
        if ingrediente:
            if nombre:
                ingrediente.nombre = nombre
            if stock:
                ingrediente.stock = stock
            db.commit()
            db.refresh(ingrediente)
        return ingrediente
    
    def borrar(self, db: Session, id: int):
        ingrediente = db.query(Ingrediente).get(id)
        if ingrediente:
            db.delete(ingrediente)
            db.commit()
        return ingrediente