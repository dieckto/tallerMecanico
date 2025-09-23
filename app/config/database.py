from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Formato de conexión:
# "mysql+pymysql://usuario:contraseña@localhost/nombre_base"

DATABASE_URL = "mysql+pymysql://root:@localhost/tallermecanico"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
