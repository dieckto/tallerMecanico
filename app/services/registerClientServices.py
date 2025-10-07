from app.controllers.clientsController import createClient


def validateClientFields(name: str, phone: str, email: str, address: str = None, assesor_id: int = None):
    if not all([name, phone, email]):
        return False, "Los campos nombre, teléfono y correo electrónico son obligatorios."
    if "@" not in email or "." not in email:
        return False, "Correo electrónico inválido."
    if len(phone) < 7:
        return False, "El número de teléfono es demasiado corto."
    return True, ""

def registerClient(name: str, phone: str, email: str, address: str = None, assesor_id: int = None):
    is_valid, message = validateClientFields(name, phone, email, address, assesor_id)
    if not is_valid:
        return is_valid, message
    else:
        if createClient(name, phone, email, address, assesor_id) == None:
            return False, "Error al registrar el cliente. Inténtalo de nuevo."
        return True, "Cliente registrado exitosamente."