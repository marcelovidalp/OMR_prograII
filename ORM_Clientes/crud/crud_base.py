from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class CRUDBase(ABC):
    @abstractmethod
    def leer(self, db: Session):
        pass

    @abstractmethod
    def agregar(self, db: Session, **kwargs):
        pass

    @abstractmethod
    def modificar(self, db: Session, id: int, **kwargs):
        pass

    @abstractmethod
    def borrar(self, db: Session, id: int):
        pass