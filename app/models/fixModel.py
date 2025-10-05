from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base, session

class Fix(Base):
    __tablename__ = "fixes"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    cost = Column(Integer, nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    car = relationship("Car", back_populates="fixes")
