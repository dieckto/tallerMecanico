from app.controllers.userController import *

def authenticate(username, password):

    user = getUserByUsername(username)
    if user and user.hashed_password == password:

        return True

    else:  

        return False

    return username == "admin" and password == "password"