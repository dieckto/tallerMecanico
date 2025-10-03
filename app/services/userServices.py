from app.controllers.userController import *

def getUserName(username: str):
    user = getUserByUsername(username)
    if user:
        return user.full_name
    return None

def getRole(id):
    
    user = getUserById(id)

    if user: 
        return user.role
    else: 
        return None