from sqlalchemy import create_engine

url = "sqlite:///mi_base_de_datos.db"

engine = create_engine(url, echo=True)
