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
        
    def modificar_usuario(self): # Método para modificar un usuario
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar Usuario")
        ventana.geometry("350x400")

        registros = self.gestor.cargar_usuarios() # Carga los usuarios registrados
        if not registros: # Verifica si hay usuarios registrados
            tk.Label(ventana, text="No hay usuarios.", font=("Arial", 12)).pack(pady=20)
            return

        nombres = [r["nombre"] for r in registros] # Lista de nombres de los usuarios
        seleccion = tk.StringVar(value=nombres[0])

        tk.Label(ventana, text="Seleccione usuario:", font=("Arial", 12)).pack(pady=5)
        ttk.Combobox(ventana, textvariable=seleccion, values=nombres).pack(fill="x", padx=20)

        edad = tk.Entry(ventana)
        actividad = tk.StringVar()
        actividad.set("Spinning")
        clases = tk.Entry(ventana)
        asistencias = tk.Entry(ventana)

        tk.Label(ventana, text="Nueva edad:").pack()
        edad.pack()
        tk.Label(ventana, text="Nueva actividad:").pack()
        ttk.Combobox(ventana, textvariable=actividad, values=["Spinning", "Fisioterapia", "Rumba", "Fortalecimiento"]).pack()
        tk.Label(ventana, text="Nuevo número de clases:").pack()
        clases.pack()
        tk.Label(ventana, text="Modificar asistencias:").pack()
        asistencias.pack()

        def guardar_cambios():  # Método para guardar los cambios realizados en el usuario
            nombre = seleccion.get() # Obtiene el nombre del usuario seleccionado
            for r in registros:
                if r["nombre"] == nombre: # Busca el usuario en los registros
                    if edad.get(): r["edad"] = edad.get()
                    if actividad.get(): r["actividad"] = actividad.get() # Actualiza la actividad del usuario
                    if clases.get(): r["clases"] = clases.get()
                    if asistencias.get(): r["asistencias"] = int(asistencias.get())
                    r["valor_pagado"] = Usuario(
                        r["nombre"], r["edad"], r["actividad"], r["clases"], r["asistencias"]
                    ).valor_pagado
            self.gestor.actualizar_usuarios(registros) # Actualiza los usuarios en el gestor
            messagebox.showinfo("Actualizado", "Usuario modificado correctamente.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_cambios).pack(pady=10)

    def mostrar_reporte_en_ventana(self):# Método para mostrar el reporte de análisis en una nueva ventana
        ventana = tk.Toplevel(self.root)
        ventana.title("Reporte de Análisis")
        ventana.geometry("1200x700")

        df = pd.read_csv("datos/datos.csv")
        if df.empty: # Verifica si el DataFrame está vacío
            tk.Label(ventana, text="No hay datos registrados aún.").pack(pady=20) 
            return

        total = len(df)
        incompletos = df[df.isnull().any(axis=1)] # Filtra los registros con datos incompletos
        promedio = df["valor_pagado"].mean()
        mayor_pago = df.loc[df["valor_pagado"].idxmax()]
        actividad_top = df["actividad"].mode()[0]
# Genera el resumen de los datos
        resumen = f""" #
 Total de usuarios: {total}
 Datos incompletos: {len(incompletos)}
 Promedio de pagos: ${promedio:,.2f}
 Actividad más popular: {actividad_top}
 Mayor pago: {mayor_pago['nombre']} - ${mayor_pago['valor_pagado']}
 Asistencias totales registradas: {df['asistencias'].sum()}
"""

        tk.Label(ventana, text=resumen, justify="left", anchor="w", font=("Arial", 11)).pack(pady=10)

        fig, axs = plt.subplots(1, 3, figsize=(15, 4))
        axs[0].hist(df["edad"], bins=10, color="lightblue", edgecolor="black")
        axs[0].set_title("Distribución de edades") #axis para la distribución de edades
        axs[0].set_xlabel("Edad")

        df["actividad"].value_counts().plot(kind="bar", ax=axs[1], color="salmon") # Gráfico de barras para la cantidad de usuarios por actividad
        axs[1].set_title("Usuarios por actividad")
        axs[1].set_ylabel("Cantidad")

        df["actividad"].value_counts().plot.pie(autopct="%1.1f%%", ax=axs[2])# Gráfico de pastel para la distribución de actividades
        axs[2].set_title("Distribución por actividad")
        axs[2].set_ylabel("")

        plt.tight_layout() # Ajusta el layout de los gráficos
        canvas = FigureCanvasTkAgg(fig, master=ventana) # Crea un canvas para mostrar los gráficos
        canvas.draw()# Añade los gráficos al canvas
        canvas.get_tk_widget().pack()

    def mostrar_listado(self): # Método para mostrar el listado de usuarios inscritos en una nueva ventana
        ventana = tk.Toplevel(self.root)
        ventana.title("Listado de Inscritos")
        ventana.geometry("500x400")

        df = pd.read_csv("datos.csv") # Carga los datos de los usuarios desde el archivo CSV
        if df.empty:
            tk.Label(ventana, text="No hay usuarios.", font=("Arial", 12)).pack(pady=20) # Verifica si hay usuarios registrados
            return

        texto = "\n".join([
            f"{r['nombre']}, Edad: {r['edad']}, Actividad: {r['actividad']}, Clases: {r['clases']}, Asistencias: {r.get('asistencias', 0)}, Pagado: ${r['valor_pagado']}"
            for _, r in df.iterrows() # Itera sobre los registros del DataFrame
        ])

        tk.Label(ventana, text="Listado de usuarios inscritos:", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Message(ventana, text=texto, width=480, font=("Arial", 11)).pack(padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
