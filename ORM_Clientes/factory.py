from abc import ABC, abstractmethod
from .models import Cliente, Pedido, Ingredientes, Menu

class Factory(ABC):
    @abstractmethod
    def crear_objeto(self):
        pass

class ClienteFactory(Factory):
    def crear_objeto(self):
        return Cliente()

class PedidoFactory(Factory):
    def crear_objeto(self):
        return Pedido()

class IngredientesFactory(Factory):
    def crear_objeto(self):
        return Ingredientes()

class MenuFactory(Factory):
    def crear_objeto(self):
        return Menu()
