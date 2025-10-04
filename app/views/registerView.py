import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from app.services.registerServices import register_user

class RegisterView:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")
        self.root.geometry("700x700")  # tamaño de la ventana
        self.root.config(bg="#f9f9f9")
        self.root.resizable(False, False)
        self.opciones_rol = ["auxiliar", "mecanico", "secretario"]

        self.fuente_titulo = font.Font(family="Segoe UI", size=18, weight="bold")
        self.fuente_normal = font.Font(family="Segoe UI", size=12)

        # Título
        self.label_titulo = tk.Label(
            self.root, text="Crear Cuenta", bg="#f9f9f9",
            font=self.fuente_titulo
        )
        self.label_titulo.pack(pady=30)

        # Username
        tk.Label(self.root, text="Nombre de usuario:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_username = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_username.pack(pady=10, ipady=8, ipadx=80)

        # Email
        tk.Label(self.root, text="Correo electrónico:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_email = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_email.pack(pady=10, ipady=8, ipadx=80)

        # Full name
        tk.Label(self.root, text="Nombre completo:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_fullname = tk.Entry(self.root, font=self.fuente_normal, justify="center")
        self.entry_fullname.pack(pady=10, ipady=8, ipadx=80)

        # Password
        tk.Label(self.root, text="Contraseña:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.entry_password = tk.Entry(self.root, show="*", font=self.fuente_normal, justify="center")
        self.entry_password.pack(pady=10, ipady=8, ipadx=80)

        # Role
        tk.Label(self.root, text="Rol:", bg="#f9f9f9", font=self.fuente_normal)\
            .pack(anchor="center")
        self.combo_role = ttk.Combobox(self.root, values=self.opciones_rol, font=self.fuente_normal, state="readonly", justify="center")
        self.combo_role.pack(pady=10, ipady=8, ipadx=80)

        # Botón de registro
        self.btn_register = tk.Button(
            self.root, text="Registrar", bg="#333333", fg="white",
            font=self.fuente_normal, relief="flat", cursor="hand2", 
            command= lambda: self.register_user()
        )  
        self.btn_register.pack(pady=30, ipadx=100, ipady=10)

        # Enlace para volver al login
        self.link_login = tk.Label(
            self.root, text="¿Ya tienes cuenta? Iniciar sesión",
            fg="blue", bg="#f9f9f9", cursor="hand2", font=("Segoe UI", 11, "underline")
        )
        self.link_login.pack(pady=10)
        self.link_login.bind("<Button-1>", lambda e: self.go_to_login())


    def register_user(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        full_name = self.entry_fullname.get()
        password = self.entry_password.get()
        role = self.combo_role.get()

        success, message = register_user(username, email, full_name, password, role)
        if success:
            messagebox.showinfo(message, message)

            for widget in self.root.winfo_children():
                widget.destroy()
            self.go_to_login()
        else:
            messagebox.showerror("Error", message)
    
    def go_to_login(self):
        for widget in self.root.winfo_children():
            widget.destroy() 
        from app.views.logginView import LoginView
        LoginView(self.root)

        
if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterView(root)
    root.mainloop()
