from sqlalchemy.orm import Session
from factory import IngredienteFactory
from models import Ingrediente

class IngredienteCRUD:
    @staticmethod
    def ver_ingredientes(session: Session):
        ingredientes = session.query(Ingrediente).all()
        if ingredientes:
            for ingrediente in ingredientes:
                print(ingrediente)
        else:
            print("No hay ingredientes registrados")

# ...existing code...
