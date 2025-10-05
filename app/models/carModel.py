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
    owner_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    owner = relationship("Clients", back_populates="cars")  
    fixes = relationship("Fix", back_populates="car", cascade="all, delete-orphan")