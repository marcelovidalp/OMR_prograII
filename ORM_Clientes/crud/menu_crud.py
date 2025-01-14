from sqlalchemy import Session, Menu
from models import Menu
from crud_base import CRUDBase
from factory import MenuFactory

class MenuCRUD(CRUDBase):
    def __init__(self):
        self.factory = MenuFactory()

    def leer(self, db: Session):
        return db.query(Menu).all()

    def agregar(self, db: Session, name: str, description: str, price: int):
        menu_existente = db.query(Menu).filter(Menu.nombre == name).first()
        menu = self.factory.crear_objeto()
        # implementar

# Función para ver todos los menús
def ver_menus():
    menus = session.query(Menu).all()
    if menus:
        for menu in menus:
            print(menu)
    else:
        print("No hay menus registrados")

# Función para agregar un nuevo menú
def agregar_menu():
    #copilot
    menu = Menu()
    menu.nombre = input("Ingrese el nombre del menu: ")
    menu.precio = float(input("Ingrese el precio del menu: "))
    session.add(menu)
    session.commit()
    print("Menu agregado correctamente")

# Función para modificar un menú existente
def modificar_menu():
    #copilot
    ver_menus()
    id_menu = int(input("Ingrese el ID del menu a modificar: "))
    menu = session.query(Menu).get(id_menu)
    if menu:
        menu.nombre = input("Ingrese el nuevo nombre del menu: ")
        menu.precio = float(input("Ingrese el nuevo precio del menu: "))
        session.commit()
        print("Menu modificado correctamente")
    else:
        print("Menu no encontrado")

# Función para borrar un menú existente
def borrar_menu():
    #copilot
    ver_menus()
    id_menu = int(input("Ingrese el ID del menu a borrar: "))
    menu = session.query(Menu).get(id_menu)
    if menu:
        session.delete(menu)
        session.commit()
        print("Menu eliminado correctamente")
    else:
        print("Menu no encontrado")