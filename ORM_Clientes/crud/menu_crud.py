from sqlalchemy import session
from ..object_creator import crear_menu

# Función para ver todos los menús
def ver_menus():
    menus = session.query(crear_menu()).all()
    if menus:
        for menu in menus:
            print(menu)
    else:
        print("No hay menus registrados")

# Función para agregar un nuevo menú
def agregar_menu():
    menu = crear_menu()
    menu.nombre = input("Ingrese el nombre del menu: ")
    menu.precio = float(input("Ingrese el precio del menu: "))
    session.add(menu)
    session.commit()
    print("Menu agregado correctamente")

# Función para modificar un menú existente
def modificar_menu():
    ver_menus()
    id_menu = int(input("Ingrese el ID del menu a modificar: "))
    menu = session.query(crear_menu()).get(id_menu)
    if menu:
        menu.nombre = input("Ingrese el nuevo nombre del menu: ")
        menu.precio = float(input("Ingrese el nuevo precio del menu: "))
        session.commit()
        print("Menu modificado correctamente")
    else:
        print("Menu no encontrado")

# Función para borrar un menú existente
def borrar_menu():
    ver_menus()
    id_menu = int(input("Ingrese el ID del menu a borrar: "))
    menu = session.query(crear_menu()).get(id_menu)
    if menu:
        session.delete(menu)
        session.commit()
        print("Menu eliminado correctamente")
    else:
        print("Menu no encontrado")