from app.models.clientModel import Clients
from app.config.database import session
from sqlalchemy.exc import IntegrityError

def createClient(name: str, phone: str, email: str, address: str = None):
    new_client = Clients(
        name=name,
        phone=phone,
        email=email,
        address=address
    )
    try:
        session.add(new_client)
        session.commit()
        return new_client
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()

    
def getClientById(client_id: int):
    client = session.query(Clients).filter(Clients.id == client_id).first()
    session.close()
    return client

def getAllClients():
    clients = session.query(Clients).all()
    session.close()
    return clients  

def updateClient(client_id: int, name: str = None, phone: str = None, email: str = None, address: str = None):
    client = session.query(Clients).filter(Clients.id == client_id).first()
    if not client:
        session.close()
        return None
    if name:
        client.name = name
    if phone:
        client.phone = phone
    if email:
        client.email = email
    if address:
        client.address = address
    try:
        session.commit()
        return client
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()