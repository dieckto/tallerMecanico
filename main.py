#crear todas las tablas que no existan en la base de datos 
from app.config.database import Base, engine
#se necesita importar el modelo para que se cree la tabla
from app.models.Users import Users
# Crear tablas en la BD si no existen
Base.metadata.create_all(engine)

#librerias para la interfaz grafica
import tkinter as tk
from app.views.logginView import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
