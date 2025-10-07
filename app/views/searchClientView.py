import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#importaciones de modulo
import app.views.mainView as MainView

#importaciones
from app.utils.placeholder import on_focus_in, on_focus_out, insert_placeholder 
from app.services.clientServices import getAllClientsServices, getClientsByNameServices, deleteClientService


class searchClientView:
    def __init__(self, root, userName= None, user= None):
        self.root = root
        self.root.title("Sistema de Clientes")
        self.root.geometry("1000x750")
        self.root.configure(bg='#f5f5f5')

        self.user = user
        self.userName= userName
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')

        
        # Colores
        self.color_fondo = '#f5f5f5'
        self.color_tarjeta = '#ffffff'
        self.color_primario = '#2c3e50'
        self.color_secundario = '#34495e'
        self.color_texto = '#2c3e50'
        self.color_texto_secundario = '#7f8c8d'
        self.color_borde = '#e0e0e0'
        self.color_hover = '#f8f9fa'
        self.color_borde_hover = '#3498db'
        
        # Configurar estilos
        self.configurar_estilos()
        
        # Crear interfaz
        self.crear_interfaz()
        
    def configurar_estilos(self):
        # Estilo para la barra de búsqueda
        self.style.configure('Busqueda.TEntry', 
                            fieldbackground='#ffffff',
                            foreground=self.color_texto,
                            borderwidth=2,
                            relief='solid',
                            padding=(15, 10))
        
        # Estilo para el botón de búsqueda
        self.style.configure('Busqueda.TButton',
                            background=self.color_primario,
                            foreground='white',
                            borderwidth=0,
                            focuscolor='none',
                            font=('Arial', 11, 'bold'),
                            padding=(20, 10))
        
        self.style.map('Busqueda.TButton',
                      background=[('active', self.color_secundario),
                                ('pressed', self.color_secundario)])
        
        # Estilo para la scrollbar
        self.style.configure('Custom.Vertical.TScrollbar',
                            background=self.color_primario,
                            darkcolor=self.color_primario,
                            lightcolor=self.color_primario,
                            troughcolor=self.color_fondo,
                            bordercolor=self.color_primario,
                            arrowcolor='white',
                            relief='flat')
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.color_fondo)
        main_frame.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Título
        titulo = tk.Label(main_frame, text="¡Bienvenido admin1!", 
                         font=('Arial', 28, 'bold'), 
                         bg=self.color_fondo,
                         fg=self.color_primario)
        titulo.pack(pady=(0, 8))
        
        # Subtítulo
        subtitulo = tk.Label(main_frame, text="Busca clientes en la base de datos", 
                            font=('Arial', 14), 
                            bg=self.color_fondo,
                            fg=self.color_texto_secundario)
        subtitulo.pack(pady=(0, 30))
        
        # Barra de búsqueda
        self.crear_barra_busqueda(main_frame)
        
        # Frame para las tarjetas de clientes
        self.crear_area_tarjetas(main_frame)
    
    def crear_barra_busqueda(self, parent):
        # Frame para contener la barra de búsqueda
        frame_busqueda = tk.Frame(parent, bg=self.color_fondo)
        frame_busqueda.pack(fill='x', pady=(0, 25))
        
        # Frame interno para centrar contenido
        frame_interno = tk.Frame(frame_busqueda, bg=self.color_fondo)
        frame_interno.pack(expand=True)
        
        # Entrada de búsqueda con icono
        frame_entry = tk.Frame(frame_interno, bg=self.color_fondo)
        frame_entry.pack(side='left', fill='x', expand=True)
        
        # Crear Entry de tkinter (no ttk) con estilo personalizado
        self.entry_busqueda = tk.Entry(frame_entry, 
                                    font=('Arial', 12),
                                    width=40,
                                    bg='#ffffff',
                                    fg='#7f8c8d',  # Color gris para placeholder
                                    relief='solid',
                                    bd=2,
                                    highlightthickness=0)
        
        # Insertar placeholder
        self.entry_busqueda.bind(insert_placeholder(self.entry_busqueda, "Buscar cliente por nombre..."))
        
        # Bind events para el placeholder
        self.entry_busqueda.bind("<FocusIn>", lambda e: on_focus_in(self.entry_busqueda, "Buscar cliente por nombre..."))
        self.entry_busqueda.bind("<FocusOut>", lambda e: on_focus_out(self.entry_busqueda, "Buscar cliente por nombre..."))
        
        self.entry_busqueda.pack(side='left', fill='x', expand=True, ipady=8)
        
        # Botón de búsqueda con estilo tkinter
        btn_buscar = tk.Button(frame_interno, 
                            text="🔍 Buscar", 
                            bg=self.color_primario,
                            fg='white',
                            font=('Arial', 11, 'bold'),
                            relief='flat',
                            bd=0,
                            padx=20,
                            pady=10,
                            cursor='hand2',
                            command=lambda: self.show_clients_by_name(self.entry_busqueda.get())
                            )
        btn_buscar.pack(side='left', padx=(10, 0))
        
        # Efecto hover para botón de búsqueda
        def on_enter_buscar(e):
            btn_buscar.config(bg=self.color_secundario)
        
        def on_leave_buscar(e):
            btn_buscar.config(bg=self.color_primario)
        
        btn_buscar.bind("<Enter>", on_enter_buscar)
        btn_buscar.bind("<Leave>", on_leave_buscar)

        # Botón regresar con estilo tkinter
        btn_regresar = tk.Button(frame_interno, 
                            text="← Regresar", 
                            bg=self.color_primario,
                            fg='white',
                            font=('Arial', 11, 'bold'),
                            relief='flat',
                            bd=0,
                            padx=20,
                            pady=10,
                            cursor='hand2',
                            command=lambda: self.go_to_main_view())
        btn_regresar.pack(side='left', padx=(10, 0))
        
        # Efecto hover para botón regresar
        def on_enter_regresar(e):
            btn_regresar.config(bg=self.color_secundario)
        
        def on_leave_regresar(e):
            btn_regresar.config(bg=self.color_primario)
        
        btn_regresar.bind("<Enter>", on_enter_regresar)
        btn_regresar.bind("<Leave>", on_leave_regresar)

    def crear_area_tarjetas(self, parent):
        # Frame contenedor principal
        contenedor_principal = tk.Frame(parent, bg=self.color_fondo)
        contenedor_principal.pack(fill='both', expand=True)
        
        # Crear canvas y scrollbar
        self.canvas = tk.Canvas(contenedor_principal, bg=self.color_fondo, highlightthickness=0)
        scrollbar = ttk.Scrollbar(contenedor_principal, orient="vertical", 
                                 command=self.canvas.yview, style='Custom.Vertical.TScrollbar')
        
        # Frame scrollable para las tarjetas
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.color_fondo)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Crear ventana centrada en el canvas
        self.canvas_frame = self.canvas.create_window(
            (self.canvas.winfo_reqwidth()//2, 0), 
            window=self.scrollable_frame, 
            anchor="n",
            width=self.canvas.winfo_reqwidth()
        )
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mostrar clientes de ejemplo
        self.show_clients()
        
        # Empaquetar canvas y scrollbar
        self.canvas.pack(side="left", fill="both", expand=True, padx=(0, 5))
        scrollbar.pack(side="right", fill="y", padx=(5, 0))
        
        # Configurar scroll con rueda del mouse
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.scrollable_frame.bind("<MouseWheel>", self._on_mousewheel)
        
        # Actualizar el centrado cuando cambie el tamaño
        self.canvas.bind("<Configure>", self._on_canvas_configure)
    
    def _on_canvas_configure(self, event):
        """Actualiza el ancho del frame scrollable cuando cambia el tamaño del canvas"""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def show_clients(self):
        # Datos de ejemplo más extensos
        clientes = getAllClientsServices()
        
        # Organizar tarjetas en grid de 2 columnas CENTRADO
        for i, cliente in enumerate(clientes):
            row = i // 2
            col = i % 2
            self.crear_tarjeta_cliente(cliente, row, col)
        
        # Configurar el grid para que las columnas se expandan igualmente
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
    
    def show_clients_by_name(self, name):
        # Datos de ejemplo más extensos
        clients, mesage = getClientsByNameServices(name)
        
        # Organizar tarjetas en grid de 2 columnas CENTRADO
        if clients == False:
            messagebox.showinfo("Búsqueda", mesage)
        else:   
            # Limpiar tarjetas anteriores
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
        
            for i, cliente in enumerate(clients):
                row = i // 2
                col = i % 2

                self.crear_tarjeta_cliente(cliente, row, col)
            
            # Configurar el grid para que las columnas se expandan igualmente
            self.scrollable_frame.grid_columnconfigure(0, weight=1)
            self.scrollable_frame.grid_columnconfigure(1, weight=1)

    def crear_tarjeta_cliente(self, cliente, row, col):
            # Frame contenedor para centrar cada tarjeta
            contenedor_tarjeta = tk.Frame(self.scrollable_frame, bg=self.color_fondo)
            contenedor_tarjeta.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            
            # Frame de la tarjeta con tamaño FIJO
            tarjeta = tk.Frame(contenedor_tarjeta, 
                            bg=self.color_tarjeta,
                            relief='solid',
                            borderwidth=1,
                            highlightbackground=self.color_borde,
                            highlightthickness=1,
                            width=400,  # Tamaño fijo
                            height=120)  # Tamaño fijo
            
            # Evitar que el frame se redimensione
            tarjeta.pack_propagate(False)
            tarjeta.pack(fill='both', expand=True)
            
            # Contenido de la tarjeta
            contenido_frame = tk.Frame(tarjeta, bg=self.color_tarjeta)
            contenido_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Frame superior para nombre e icono
            frame_superior = tk.Frame(contenido_frame, bg=self.color_tarjeta)
            frame_superior.pack(fill='x', pady=(0, 12))
            
            # Nombre del cliente
            nombre_label = tk.Label(frame_superior, 
                                text=cliente["Nombre"],
                                font=('Arial', 16, 'bold'),
                                bg=self.color_tarjeta,
                                fg=self.color_primario,
                                anchor='w')
            nombre_label.pack(side='left', fill='x', expand=True)
            
            # Icono de usuario
            icono_label = tk.Label(frame_superior, text="👤", 
                                font=('Arial', 20), 
                                bg=self.color_tarjeta)
            icono_label.pack(side='right', padx=(10, 0))
            
            # Línea separadora
            separador = tk.Frame(contenido_frame, height=1, bg=self.color_borde)
            separador.pack(fill='x', pady=(0, 12))
            
            # Frame inferior para asesor y botón eliminar
            frame_inferior = tk.Frame(contenido_frame, bg=self.color_tarjeta)
            frame_inferior.pack(fill='x', side='bottom')
            
            # Asesor asignado
            asesor_label = tk.Label(frame_inferior,
                                text=f"👨‍💼 Asesor: {cliente['Asesor']}",
                                font=('Arial', 12),
                                bg=self.color_tarjeta,
                                fg=self.color_texto_secundario,
                                anchor='w')
            asesor_label.pack(side='left', fill='x', expand=True)
            
            # Botón eliminar en la parte inferior derecha
            btn_eliminar = tk.Button(frame_inferior,
                                text="Eliminar",
                                font=('Arial', 10),
                                bg='#e74c3c',
                                fg='white',
                                relief='flat',
                                bd=0,
                                padx=12,
                                pady=4,
                                cursor='hand2',
                                command=lambda: self.delte_client(cliente['id'])
                                )
            btn_eliminar.pack(side='right', padx=(10, 0))
            
            # Hover effect MEJORADO - solo cambia colores, no tamaños
            def on_enter(e):
                tarjeta.configure(highlightbackground=self.color_borde_hover,
                                highlightthickness=2)
                tarjeta.configure(bg=self.color_hover)
                contenido_frame.configure(bg=self.color_hover)
                frame_superior.configure(bg=self.color_hover)
                frame_inferior.configure(bg=self.color_hover)
                nombre_label.configure(bg=self.color_hover)
                icono_label.configure(bg=self.color_hover)
                asesor_label.configure(bg=self.color_hover)
                separador.configure(bg=self.color_borde_hover)
            
            def on_leave(e):
                tarjeta.configure(highlightbackground=self.color_borde,
                                highlightthickness=1)
                tarjeta.configure(bg=self.color_tarjeta)
                contenido_frame.configure(bg=self.color_tarjeta)
                frame_superior.configure(bg=self.color_tarjeta)
                frame_inferior.configure(bg=self.color_tarjeta)
                nombre_label.configure(bg=self.color_tarjeta)
                icono_label.configure(bg=self.color_tarjeta)
                asesor_label.configure(bg=self.color_tarjeta)
                separador.configure(bg=self.color_borde)
            
            # Aplicar eventos hover a toda la tarjeta
            tarjeta.bind("<Enter>", on_enter)
            tarjeta.bind("<Leave>", on_leave)
            contenido_frame.bind("<Enter>", on_enter)
            contenido_frame.bind("<Leave>", on_leave)
            frame_superior.bind("<Enter>", on_enter)
            frame_superior.bind("<Leave>", on_leave)
            frame_inferior.bind("<Enter>", on_enter)
            frame_inferior.bind("<Leave>", on_leave)
            nombre_label.bind("<Enter>", on_enter)
            nombre_label.bind("<Leave>", on_leave)
            icono_label.bind("<Enter>", on_enter)
            icono_label.bind("<Leave>", on_leave)
            asesor_label.bind("<Enter>", on_enter)
            asesor_label.bind("<Leave>", on_leave)
    
    def delte_client(self, client_id):
        success, message = deleteClientService(client_id)
        print(client_id)
        if success:
            messagebox.showinfo("Eliminar", message)
            # Refrescar la lista de clientes
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            self.show_clients()
        else:
            messagebox.showerror("Error", message)

    def go_to_main_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MainView.MainView(self.root, self.userName, self.user)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteInterfaz(root)
    root.mainloop()