from .factory import ClienteFactory, PedidoFactory, IngredientesFactory, MenuFactory
from models import Pedido, Cliente, Ingredientes, Menu
# Crear instancias de las fábricas
cliente_factory = ClienteFactory()
pedido_factory = PedidoFactory()
ingredientes_factory = IngredientesFactory()
menu_factory = MenuFactory()

# Funciones para crear objetos
def crear_cliente() -> Cliente:
    return cliente_factory.crear_objeto()

def crear_pedido() -> Pedido:
    return pedido_factory.crear_objeto()

def crear_ingrediente() -> Ingredientes:
    return ingredientes_factory.crear_objeto()

def crear_menu() -> Menu:
    return menu_factory.crear_objeto()
