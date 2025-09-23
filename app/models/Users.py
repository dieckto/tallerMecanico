from sqlalchemy import Column, Integer, String
from app.config.database import Base, session



class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # e.g., 'admin', 'mechanic', 'customer'



def create_admin_user():
    cliente = Users(
        username="admin",
        email="blablabla@gmail.com",
        full_name="Admin", 
        hashed_password="admin",
        role="admin"
    )
    session.add(cliente)    
    session.commit()
    session.close()