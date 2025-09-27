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


def deleteUserById(user_id: int):
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        session.close()
        return False
    session.delete(user)
    session.commit()
    session.close()
    return True