import tkinter as tk
from tkinter import font
from app.services.loginService import authenticate
from app.views.mainView import MainView
from app.views.registerView import RegisterView
from app.services.getUserName import getUserName


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x350")
        self.root.config(bg="#f9f9f9")
        self.root.resizable(False, False)

        self.fuente = font.Font(family="Segoe UI", size=11)

        self.create_widgets()  # Aquí se crean los widgets

    def create_widgets(self):
        # Limpiar widgets antiguos (por si se reconstruye)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Contenedor
        self.frame = tk.Frame(self.root, bg="#f9f9f9")
        self.frame.pack(expand=True)

        # Título
        self.lbl_title = tk.Label(self.frame, text="Iniciar Sesión",
                                  bg="#f9f9f9", fg="#333",
                                  font=("Segoe UI", 16, "bold"))
        self.lbl_title.pack(pady=(0, 20))

        # Campo usuario
        self.entry_user = tk.Entry(self.frame, font=self.fuente, bd=0,
                                   highlightthickness=1, highlightbackground="#ccc",
                                   relief="flat")
        self.entry_user.pack(pady=10, ipadx=10, ipady=8, fill="x")

        # Campo contraseña
        self.entry_pass = tk.Entry(self.frame, font=self.fuente, bd=0,
                                   highlightthickness=1, highlightbackground="#ccc",
                                   show="*", relief="flat")
        self.entry_pass.pack(pady=10, ipadx=10, ipady=8, fill="x")

        # Botón login
        self.btn_login = tk.Button(self.frame, text="Entrar", font=self.fuente,
                                   bg="#333", fg="white", relief="flat",
                                   cursor="hand2", activebackground="#555",
                                   activeforeground="white",
                                   command=lambda: self.login(self.entry_user.get()))
        self.btn_login.pack(pady=20, ipadx=10, ipady=5, fill="x")

        self.lbl_link = tk.Label(self.frame, text="Crear cuenta", fg="#1a73e8",
                                 bg="#f9f9f9", font=("Segoe UI", 10, "underline"),
                                 cursor="hand2")
        self.lbl_link.pack(pady=(10, 0))
        self.lbl_link.bind("<Button-1>", lambda e: self.crear_cuenta())

    def login(self, user):
        userName = getUserName(user)
        contrasena = self.entry_pass.get()
        if authenticate(user, contrasena):
            # Limpiar login y abrir MainView
            for widget in self.root.winfo_children():
                widget.destroy()
            MainView(self.root, userName)
        else:
            self.errorLogin()
             #
            print("Login fallido")
    def errorLogin(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.viewLoginError()

    def viewLoginError(self):

        self.frame = tk.Frame(self.root, bg="#f9f9f9")
        self.frame.pack(expand=True)

        self.lbl_error = tk.Label(self.frame, text="Usuario o contraseña incorrectos",
                                  bg="#f9f9f9", fg="red", font=("Segoe UI", 10))
        self.lbl_error.pack(pady=(0, 10))

        self.lbl_link = tk.Label(self.frame, text="Crear cuenta", fg="#1a73e8",
                                 bg="#f9f9f9", font=("Segoe UI", 10, "underline"),
                                 cursor="hand2")
        self.lbl_link.pack(pady=(10, 0))

         # Botón login
        self.btn_Errorlogin = tk.Button(self.frame, text="aceptar", font=self.fuente,
                                   bg="#333", fg="white", relief="flat",
                                   cursor="hand2", activebackground="#555",
                                   activeforeground="white",
                                   command=lambda: self.create_widgets())
        self.btn_Errorlogin.pack(pady=20, ipadx=10, ipady=5, fill="x")

    def crear_cuenta(self):
        for widget in self.root.winfo_children():
            widget.destroy() 
        RegisterView(self.root)
