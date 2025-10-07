import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

#importaciones de modulo
import app.views.mainView as MainView

from app.services.userServices import getUserId
from app.services.registerClientServices import registerClient


class RegisterNewClient:
    def __init__(self, root, userName= None, user= None):
        self.root = root
        self.root.title("Registro de cliente")
        self.root.geometry("700x700")  # tamaño de la ventana
        self.root.config(bg="#f9f9f9")
        self.root.resizable(False, False)

        #variables user (necesries for the main view)
        self.user = user
        self.userName= userName
        self.assesor_id = getUserId(user)

        self.fuente_titulo = font.Font(family="Segoe UI", size=18, weight="bold")
        self.fuente_normal = font.Font(family="Segoe UI", size=12)

        # Título
        self.label_titulo = tk.Label(
            self.root, text="Registrar Cliente", bg="#f9f9f9",
            font=self.fuente_titulo
        )
        self.label_titulo.pack(pady=30)

        # Username
        tk.Label(self.root, text="Nombre de Cliente:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_fullName = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_fullName.pack(pady=10, ipady=8, ipadx=80)

        # Email
        tk.Label(self.root, text="Correo electrónico:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_email = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_email.pack(pady=10, ipady=8, ipadx=80)

        # Full name
        tk.Label(self.root, text="Número de telefono:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_phone = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_phone.pack(pady=10, ipady=8, ipadx=80)

        tk.Label(self.root, text="Dirección:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_address = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_address.pack(pady=10, ipady=8, ipadx=80)

        # Botón de registro
        self.btn_register = tk.Button(
            self.root, text="Registrar", bg="#333333", fg="white",
            font=self.fuente_normal, relief="flat", cursor="hand2", 
            command= lambda: self.register_client()
        )  
        self.btn_register.pack(pady=30, ipadx=100, ipady=10)

        # Enlace para volver al login
        self.link_main_view = tk.Label(
            self.root, text="cancelar",
            fg="blue", bg="#f9f9f9", cursor="hand2", font=("Segoe UI", 11, "underline")
        )
        self.link_main_view.pack(pady=10)
        self.link_main_view.bind("<Button-1>", lambda e: self.go_to_main_view())


    def register_client(self):
        username = self.entry_fullName.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        

        success, message = registerClient(username, phone, email, address, self.assesor_id)
        if success:
            messagebox.showinfo(message, message)

            for widget in self.root.winfo_children():
                widget.destroy()
            self.go_to_main_view()
        else:
            messagebox.showerror("Error", message)
    
    def go_to_main_view(self):
        for widget in self.root.winfo_children():
            widget.destroy() 
        MainView.MainView(self.root, self.userName, self.user)

        
if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterView(root)
    root.mainloop()
