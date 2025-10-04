from app.models.carModel import Cars
from app.config.database import session
from sqlalchemy.exc import IntegrityError

def createCar(brand: str, model: str, year: int, matricula: str, ownerid: int):
    new_car = Cars(
        brand=brand,
        model=model,
        year=year,
        matricula=matricula,
        ownerid=ownerid
    )
    try:
        session.add(new_car)
        session.commit()
        return new_car
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()

    
def getCarById(car_id: int):
    car = session.query(Cars).filter(Cars.id == car_id).first()
    session.close()
    return car

def getAllCars():
    cars = session.query(Cars).all()
    session.close()
    return cars

def updateCar(car_id: int, brand: str = None, model: str = None, year: int = None, matricula: str = None, ownerid: int = None):
    car = session.query(Cars).filter(Cars.id == car_id).first()
    if not car:
        session.close()
        return None
    if brand:
        car.brand = brand
    if model:
        car.model = model
    if year:
        car.year = year
    if matricula:
        car.matricula = matricula
    if ownerid:
        car.ownerid = ownerid
    try:
        session.commit()
        return car
    except IntegrityError:
        session.rollback()
        return None
    finally:
        session.close()



def deleteCar(car_id: int):
    car = session.query(Cars).filter(Cars.id == car_id).first()
    if not car:
        session.close()
        return False
    session.delete(car)
    session.commit()
    session.close()
    return True

def getCarsByOwnerId(owner_id: int):
    cars = session.query(Cars).filter(Cars.ownerid == owner_id).all()
    session.close()
    return cars

 