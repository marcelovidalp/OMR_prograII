from factory import ClienteFactory
from models import Cliente

#en el linux no se instala con pip install customtkinter
from sqlalchemy.orm import Session


class ClienteCRUD:
    @staticmethod
    def crear_cliente():
        return ClienteFactory().crear_objeto()
    
    @staticmethod
    def ver_clientes(session: Session):
        clientes = session.query(Cliente).all()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("No hay clientes registrados")

    @staticmethod
    def update_cliente(self, session: Session, cliente: Cliente):
        session.add(cliente)
        session.commit()
        print("Cliente actualizado correctamente")
    
    @staticmethod
    def delete_cliente(self, session: Session, cliente: Cliente):
        session.delete(cliente)
        session.commit()
        print("Cliente eliminado correctamente")

