from .factory import ClienteFactory, PedidoFactory, IngredientesFactory, MenuFactory

# Crear instancias de las fábricas
cliente_factory = ClienteFactory()
pedido_factory = PedidoFactory()
ingredientes_factory = IngredientesFactory()
menu_factory = MenuFactory()

# Funciones para crear objetos
def crear_cliente():
    return cliente_factory.crear_objeto()

def crear_pedido():
    return pedido_factory.crear_objeto()

def crear_ingrediente():
    return ingredientes_factory.crear_objeto()

def crear_menu():
    return menu_factory.crear_objeto()
