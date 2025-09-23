from app.models.Users import Users
from app.config.database import session
from sqlalchemy.exc import IntegrityError

def createUser(username: str, email: str, full_name: str, hashed_password: str, role: str):
    new_user = Users(
        username=username,
        email=email,
        full_name=full_name,
        hashed_password=hashed_password,
        role=role
    )
    try:
        session.add(new_user)
        session.commit()
        return new_user
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()

def getUserById(user_id: int):
    user = session.query(Users).filter(Users.id == user_id).first()
    session.close()
    return user

def getAllUsers():
    users = session.query(Users).all()
    session.close()
    return users

def updateUser(user_id: int, username: str = None, email: str = None, full_name: str = None, hashed_password: str = None, role: str = None):
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        session.close()
        return None
    if username:
        user.username = username
    if email:
        user.email = email
    if full_name:
        user.full_name = full_name
    if hashed_password:
        user.hashed_password = hashed_password
    if role:
        user.role = role
    try:
        session.commit()
        return user
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()

def deleteUser(user_id: int):
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        session.close()
        return False
    else:
        try: 

            session.delete(user)
            session.commit()
            session.close()
            return True
        except:
            session.rollback()
            session.close()
            return False

