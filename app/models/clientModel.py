from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base, session
from sqlalchemy.orm import relationship

class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    address = Column(String(255), nullable=True)
    cars = relationship("Car", back_populates="owner", cascade="all, delete-orphan")
    assesorid = Column(Integer, ForeignKey("users.id"),nullable=True)  # ID del asesor asignado
    assesor = relationship("Users", back_populates= "clients")  # Relación con el modelo Users
    fixes = relationship("Fix", back_populates="client", cascade="all, delete-orphan")