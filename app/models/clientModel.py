from sqlalchemy import Column, Integer, String
from app.config.database import Base, session

class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    address = Column(String(255), nullable=True)