from app.controllers.clientsController import getAllClients, getClientsByName, deleteClient
from app.services.userServices import getUserNameById

def getAllClientsServices():
    try:
        clients = getAllClients()
        all_clients = []
        for client in clients:
            clientName = client.name
            assesorid = client.assesor_id
            assesor = getUserNameById(assesorid) if assesorid else "N/A"
            all_clients.append({"Nombre":clientName, "Asesor":assesor, "id":client.id})
        return all_clients
    except Exception as e:
        return [], str(e)


def getClientsByNameServices(name: str):
    try:
        clients = getClientsByName(name)
        matched_clients = []
        for client in clients:
            clientName = client.name
            assesorid = client.assesor_id
            assesor = getUserNameById(assesorid) if assesorid else "N/A"
            matched_clients.append({"Nombre":clientName, "Asesor":assesor, "id":client.id})
        return matched_clients, "Clientes encontrados."
    except Exception as e:
        return [], str(e)

def deleteClientService(client_id: int):
    try:
        result = deleteClient(client_id)
        if result is None:
            return False, "Error al eliminar el cliente. Inténtalo de nuevo."
        return True, "Cliente eliminado exitosamente."
    except Exception as e:
        return False, str(e)