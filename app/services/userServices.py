from app.controllers.userController import *

def getUserName(username: str):
    user = getUserByUsername(username)
    if user:
        return user.full_name
    return None

def getRole(username: str):
    
    user = getUserByUsername(username)

    if user: 
        return user.role
    else: 
        return None
    
def getUserId(username: str):
    user = getUserByUsername(username)
    if user:
        return user.id
    return None