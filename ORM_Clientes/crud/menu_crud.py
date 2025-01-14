from sqlalchemy import Session, Menu
from models import Menu, Ingredientes
from crud_base import CRUDBase
from factory import MenuFactory

class MenuCRUD(CRUDBase):
    def __init__(self):
        self.factory = MenuFactory()

    def leer(self, db: Session):
        return db.query(Menu).all()

    def agregar(self, db: Session, name: str, description: str, price: int, ingredientes_name: list):
        ingredientes_nes = []
        for nombre in ingredientes_name:
            ingrediente = db.query(Ingredientes).filter(Ingredientes.nombre == nombre).first()
            if ingrediente:
                ingredientes_nes.append(ingrediente)
            if ingrediente.stock <= 0:
                print(f"No hay stock suficiente de {ingrediente.nombre}")
                return None
            ingredientes_nes.append(ingrediente)

        for ingrediente in ingredientes_nes:
            ingrediente.stock -= 1

        menu = self.factory.crear_objeto()
        menu.nombre = name
        menu.descripcion = description
        menu.precio = price
        menu.ingredientes = ingredientes_nes

        db.add(menu)
        db.commit()
        db.refresh(menu)
        return menu
