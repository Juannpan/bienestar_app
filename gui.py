import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from logica import Usuario, GestorUsuarios

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Centro de Bienestar Comunitario")
        self.root.geometry("400x500")
        self.gestor = GestorUsuarios()  # Instancia del gestor de usuarios
        self.nombre = tk.Entry(root, font=("Arial", 12)) # Campo para el nombre del usuario
        self.edad = tk.Entry(root, font=("Arial", 12))# Campo para la edad del usuario
        self.actividad = tk.StringVar()# Variable para la actividad seleccionada
        self.actividad.set("Spinning")# Valor por defecto de la actividad
        self.clases = tk.Entry(root, font=("Arial", 12))# Campo para el número de clases

        self.crear_widgets()

    def crear_widgets(self):# Método para crear los widgets de la interfaz
        tk.Label(self.root, text="Nombre:", font=("Arial", 12)).pack(pady=5)
        self.nombre.pack(fill="x", padx=20)

        tk.Label(self.root, text="Edad:", font=("Arial", 12)).pack(pady=5)
        self.edad.pack(fill="x", padx=20)

        tk.Label(self.root, text="Actividad:", font=("Arial", 12)).pack(pady=5)
        ttk.Combobox(self.root, textvariable=self.actividad, values=["Spinning", "Fisioterapia", "Rumba", "Fortalecimiento"]).pack(fill="x", padx=20)

        tk.Label(self.root, text="Número de clases:", font=("Arial", 12)).pack(pady=5)
        self.clases.pack(fill="x", padx=20)

        tk.Button(self.root, text="Registrar Usuario", font=("Arial", 12), command=self.registrar).pack(pady=10, fill="x", padx=50)
        tk.Button(self.root, text="Modificaciones", font=("Arial", 12), command=self.abrir_modificaciones).pack(pady=5, fill="x", padx=50)
        tk.Button(self.root, text="Mostrar Reporte", font=("Arial", 12), command=self.mostrar_reporte_en_ventana).pack(pady=5, fill="x", padx=50)
        tk.Button(self.root, text="Salir", font=("Arial", 12), command=self.root.quit).pack(pady=10, fill="x", padx=50)

    def registrar(self): # Método para registrar un usuario
        try: # Verifica si los campos están llenos
            if int(self.edad.get()) < 15: # Verifica si la edad es menor a 15
                messagebox.showwarning("Edad mínima", "La edad mínima para registrarse es 15 años.") 
                return
            user = Usuario(self.nombre.get(), self.edad.get(), self.actividad.get(), self.clases.get()) # Crea una instancia de Usuario
            self.gestor.guardar_usuario(user) # Guarda el usuario usando el gestor
            messagebox.showinfo("Registro exitoso", f"Usuario registrado correctamente. Total a pagar: ${user.valor_pagado}") 
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def abrir_modificaciones(self): # Método para abrir la ventana de modificaciones
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificaciones")
        ventana.geometry("300x250")

        tk.Button(ventana, text="Eliminar Usuario", font=("Arial", 12), command=self.eliminar).pack(pady=10, fill="x", padx=30)
        tk.Button(ventana, text="Registrar Asistencia", font=("Arial", 12), command=self.asistencia).pack(pady=10, fill="x", padx=30)
        tk.Button(ventana, text="Modificar Usuario", font=("Arial", 12), command=self.modificar_usuario).pack(pady=10, fill="x", padx=30)
        tk.Button(ventana, text="Mostrar Listado", font=("Arial", 12), command=self.mostrar_listado).pack(pady=10, fill="x", padx=30)
        
    def eliminar(self): # Método para eliminar un usuario
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Usuario")
        registros = self.gestor.cargar_usuarios()
        nombres = [r["nombre"] for r in registros]
        seleccion = tk.StringVar(value=nombres[0] if nombres else "") # Variable para la selección del usuario a eliminar

        ttk.Combobox(ventana, textvariable=seleccion, values=nombres).pack(fill="x", padx=20, pady=10) # Combobox para seleccionar el usuario a eliminar

        def confirmar(): # Método para confirmar la eliminación del usuario
            self.gestor.eliminar_usuario(seleccion.get()) # Llama al método del gestor para eliminar el usuario
            messagebox.showinfo("Eliminado", "Usuario eliminado correctamente.")
            ventana.destroy()

        tk.Button(ventana, text="Eliminar", command=confirmar).pack(pady=10)

    def asistencia(self): # Método para registrar la asistencia de un usuario
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Asistencia")
        registros = self.gestor.cargar_usuarios() # Carga los usuarios registrados
        nombres = [r["nombre"] for r in registros]
        seleccion = tk.StringVar(value=nombres[0] if nombres else "") # Variable para la selección del usuario

        ttk.Combobox(ventana, textvariable=seleccion, values=nombres).pack(fill="x", padx=20, pady=10) # Combobox para seleccionar el usuario

        def registrar(): # Método para registrar la asistencia del usuario seleccionado
            self.gestor.registrar_asistencia(seleccion.get())
            messagebox.showinfo("Asistencia", "Asistencia registrada.")
            ventana.destroy()

        tk.Button(ventana, text="Registrar", command=registrar).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
