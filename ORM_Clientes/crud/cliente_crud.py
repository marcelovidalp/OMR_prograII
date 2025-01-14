from factory import ClienteFactory
from models import Cliente
from crud_base import CRUDBase
from sqlalchemy.orm import Session

class ClienteCRUD(CRUDBase):
    def __init__(self):
        self.factory = ClienteFactory()

    def agregar(self, db: Session, name: str, email: str):
        cliente_existente = db.query(Cliente).filter(Cliente.email == email or cliente.nombre == name).first()
        if not cliente_existente:
            cliente = self.factory.crear_objeto(name, email)
            cliente.nombre = name
            cliente.email = email
            db.add(cliente)
            db.commit()
            db.refresh(cliente)
            return cliente
        if cliente_existente:
            print("Cliente ya registrado")
            return cliente_existente
        
    
    def leer(self, db: Session):
        clientes = db.query(Cliente).all()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("No hay clientes registrados")
    
    def modificar(self, db: Session, cliente: Cliente, new_name: str = None, new_email: str = None):
        if not cliente:
            print("Cliente no encontrado")
            return None

        if not new_name and not new_email:
            print("No se ingresaron nuevos datos")
            return None

        if new_name:
            cliente.nombre = new_name
        if new_email:
            cliente.email = new_email

        db.commit()
        print("Cliente actualizado correctamente")
        return cliente

    def borrar(self, db: Session):
        cliente = db.query(Cliente).get(id)
        try:
            db.delete(cliente)
            db.commit()
            print("Cliente eliminado correctamente")
        except Exception as e:
            print("Error al eliminar cliente")

