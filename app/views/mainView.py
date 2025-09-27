import tkinter as tk
#NOTA: usar import de modulo puede evitar el error de importacion ciclica
import app.views.logginView as logginView


class MainView:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title("Main aplication")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variables para controlar el estado del menú
        self.menu_desplegado = False
        self.ancho_menu = 250

        #variable usuario
        self.usuario = usuario
        
        # Crear el frame principal
        self.frame_principal = tk.Frame(root, bg="#f0f0f0")
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Crear el menú lateral (inicialmente oculto)
        self.menu_lateral = tk.Frame(
            self.frame_principal, 
            bg="#2c3e50", 
            width=self.ancho_menu
        )
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_lateral.pack_forget()  # Ocultar inicialmente
        
        # Crear el contenido principal
        self.contenido_principal = tk.Frame(self.frame_principal, bg="#ecf0f1")
        self.contenido_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.crear_boton_menu()
        self.crear_menu_lateral()
        self.crear_contenido_principal()
        
    def crear_boton_menu(self):
        """Crear el botón hamburguesa para abrir/cerrar el menú"""
        self.btn_menu = tk.Button(
            self.contenido_principal,
            text="☰",
            font=("Arial", 20),
            bg="#3498db",
            fg="white",
            bd=0,
            width=3,
            height=1,
            command=self.toggle_menu,
            cursor="hand2"
        )
        self.btn_menu.place(x=10, y=10)
        
    def crear_menu_lateral(self):
        """Crear los elementos del menú lateral"""
        titulo = tk.Label(
            self.menu_lateral,
            text="MENÚ",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=20
        )
        titulo.pack(fill=tk.X)
    
        opciones = [
            "🏠 Inicio",
            "👤 Perfil",
            "📊 Dashboard",
            "⚙️ Configuración",
            "📝 Reportes",
            "❓ Ayuda",
            "🚪 Salir"
        ]
        
        for opcion in opciones:
            btn = tk.Button(
                self.menu_lateral,
                text=opcion,
                font=("Arial", 12),
                bg="#34495e",
                fg="white",
                bd=0,
                pady=15,
                anchor="w",
                padx=20,
                command=lambda opt=opcion: self.seleccionar_opcion(opt),
                cursor="hand2"
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
            
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#4a6b8a"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#34495e"))
    
    def crear_contenido_principal(self):
        """Crear el contenido de la ventana principal"""

        titulo_principal = tk.Label(
            self.contenido_principal,
            text=f"¡ bienvenido {self.usuario}!",
            font=("Arial", 24, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        titulo_principal.pack(pady=(80, 20))
        
        # Área de contenido
        self.area_contenido = tk.Frame(
            self.contenido_principal,
            bg="white",
            relief=tk.RAISED,
            bd=1
        )
        self.area_contenido.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Texto de bienvenida
        self.etiqueta_contenido = tk.Label(
            self.area_contenido,
            text="Bienvenido!\n\nHaz clic en el botón ☰ para abrir el menú lateral.\n\nSelecciona cualquier opción del menú para ver el contenido aquí.",
            font=("Arial", 14),
            bg="white",
            fg="#34495e",
            justify=tk.CENTER,
            wraplength=400
        )
        self.etiqueta_contenido.pack(expand=True)
    
    def toggle_menu(self):
        """Alternar entre mostrar y ocultar el menú"""
        if self.menu_desplegado:
            self.ocultar_menu()
        else:
            self.mostrar_menu()
    
    def mostrar_menu(self):
        """Mostrar el menú lateral con animación"""
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y, before=self.contenido_principal)
        self.menu_desplegado = True
        
        # Cambiar el ícono del botón
        self.btn_menu.configure(text="✕")
    
    def ocultar_menu(self):
        """Ocultar el menú lateral"""
        self.menu_lateral.pack_forget()
        self.menu_desplegado = False
        
        # Cambiar el ícono del botón
        self.btn_menu.configure(text="☰")
    
    def seleccionar_opcion(self, opcion):
        """Manejar la selección de opciones del menú"""

        if opcion == "🚪 Salir":
            for widget in self.root.winfo_children():
                widget.destroy()
                logginView.LoginView(self.root)
            return
        contenidos = {
            "🏠 Inicio": "Has seleccionado INICIO\n\nEsta es la página principal de la aplicación.",
            "👤 Perfil": "Has seleccionado PERFIL\n\nAquí puedes ver y editar tu información personal.",
            "📊 Dashboard": "Has seleccionado DASHBOARD\n\nVista general de estadísticas y métricas importantes.",
            "⚙️ Configuración": "Has seleccionado CONFIGURACIÓN\n\nAjusta las preferencias de la aplicación.",
            "📝 Reportes": "Has seleccionado REPORTES\n\nGenera y visualiza reportes personalizados.",
            "❓ Ayuda": "Has seleccionado AYUDA\n\n¿Necesitas ayuda? Consulta nuestra documentación."
        }
        
        
        texto = contenidos.get(opcion, f"Seleccionaste: {opcion}")
        self.etiqueta_contenido.configure(text=texto)
        
        # Ocultar el menú después de seleccionar una opción
        self.ocultar_menu()

# Versión alternativa con animación suave