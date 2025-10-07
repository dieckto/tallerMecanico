#crear todas las tablas que no existan en la base de datos 
from app.config.database import Base, engine
#modelos para la creacion de tablas
from app.models.Users import Users
from app.models.clientModel import Clients
from app.models.carModel import Car
from app.models.fixModel import Fix

# Crear tablas en la BD si no existen
Base.metadata.create_all(engine)

#librerias para la interfaz grafica
import tkinter as tk
from app.views.logginView import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
