from app.controllers.userController import getUserByUsername

def getUserName(username: str):
    user = getUserByUsername(username)
    if user:
        return user.full_name
    return None