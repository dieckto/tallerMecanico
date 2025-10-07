from app.controllers.userController import *

def validateFields(username, email, full_name, password, role):
    if not all([username, email, full_name, password, role]):
        return False, "Todos los campos son obligatorios."
    if "@" not in email or "." not in email:
        return False, "Correo electrónico inválido."
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    return True, ""

def register_user(username, email, full_name, password, role):
    is_valid, message = validateFields(username, email, full_name, password, role)
    if not is_valid:
        return False, message

    existing_user = getUserByUsername(username)
    if existing_user:
        return False, "El nombre de usuario ya existe."

    existing_email = getUserByEmail(email)
    if existing_email:
        return False, "El correo electrónico ya está registrado."

    if createUser(username, email, full_name, password, role) == None:
        return False, "Error al registrar el usuario. Inténtalo de nuevo."
    else:
        return True, "Usuario registrado exitosamente."