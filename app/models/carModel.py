from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base, session



class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    matricula = Column(String(100), unique=True, index=True, nullable=False)
    ownerid = Column(Integer, ForeignKey("clients.id"), nullable=False) 
    owner = relationship("Clients", back_populates="cars")