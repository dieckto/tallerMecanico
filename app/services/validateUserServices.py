from app.services.userServices import getRole

def validateRange(role, action):
    if role == "admin":
        return True
    elif role == "secretario":
        if action == "register_admin":
            return False
        elif action == "register_client":
            return True
        elif action == "register_car":
            return True
        elif action == "puede ver pestaña de clientes y vehiculo, no puede eliminar ni editar ":
            pass
        mecanico= "solo puede meterse al de reparaciones no puede editar ni eliminar nada puede hacer nueva reparación y editar y buscar"
    else:
        return False