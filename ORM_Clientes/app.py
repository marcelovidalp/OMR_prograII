import customtkinter as ctk
from customtkinter import messagebox
import sqlalchemy 

# Definición de la clase principal de la aplicación
class MainApp():
    def __init__(self):
        self.window = ctk.CTk(title="ORM Clientes")
        self.window.geometry("800x600")
        self.window.resizable(0,0)
        self.window.config(bg="lightblue")
        self.window.mainloop()

    # Método para crear los widgets de la interfaz
    def create_widgets(self):
        self.lbl_title = ctk.CTkLabel(self.window, text="ORM Clientes", font=("Arial", 24), bg="lightblue")
        self.lbl_title.pack(pady=10)
        
        self.btn_clientes = ctk.CTkButton(self.window, text="Clientes", font=("Arial", 16), bg="lightblue", command=self.show_clientes)
        self.btn_clientes.pack(pady=10)
        
        self.btn_pedidos = ctk.CTkButton(self.window, text="Pedidos", font=("Arial", 16), bg="lightblue", command=self.show_pedidos)
        self.btn_pedidos.pack(pady=10)
        
        self.btn_ingredientes = ctk.CTkButton(self.window, text="Ingredientes", font=("Arial", 16), bg="lightblue", command=self.show_ingredientes)
        self.btn_ingredientes.pack(pady=10)
        
        self.btn_menu = ctk.CTkButton(self.window, text="Menu", font=("Arial", 16), bg="lightblue", command=self.show_menu)
        self.btn_menu.pack(pady=10)