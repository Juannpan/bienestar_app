import csv

class Usuario:
    #Almacenamiento de datos del usuario
    
    def __init__(self, nombre, edad, actividad, clases, asistencias=0):
        self.nombre = nombre
        self.edad = int(edad)
        self.actividad = actividad
        self.clases = int(clases)
        self.asistencias = int(asistencias)
        self.valor_pagado = self.calcular_pago()

    def calcular_pago(self):
        #calculadora de pago. Básicamente multiplica el número de días por el precio fijo de la clase.
        precios = {
            "Spinning": 7000,
            "Fisioterapia": 10000,
            "Rumba": 5000,
            "Fortalecimiento": 6500
        }
        return precios.get(self.actividad, 0) * self.clases

    def to_dict(self):
        #convierte todo a diccionario
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "actividad": self.actividad,
            "clases": self.clases,
            "valor_pagado": self.valor_pagado,
            "asistencias": self.asistencias
        }
        
#clase para gestionar el diccionario de usuarios       
class GestorUsuarios:
    def __init__(self, archivo="datos/datos.csv"):
        self.archivo = archivo
        
    #cargar los usuarios desde el archivo csv
    def cargar_usuarios(self):
        try:
            with open(self.archivo, mode="r", newline='', encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []
    #guarda usuarios en el csv 
    def guardar_usuario(self, usuario: Usuario):
        registros = self.cargar_usuarios()
        registros.append(usuario.to_dict())
        self._guardar_csv(registros)
        
    #crea el archivo csv con índice por columna    
    def _guardar_csv(self, registros):
            with open(self.archivo, mode="w", newline='', encoding="utf-8") as f:
                fieldnames = ["nombre", "edad", "actividad", "clases", "valor_pagado", "asistencias"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(registros)
    
    #Básicamente re-acciona _guardar_csv para modificar            
    def actualizar_usuarios(self, registros):
        self._guardar_csv(registros)

    #carga los usarios, filtra el nombre y guarda el archivo nuevamente sin esa fila
    def eliminar_usuario(self, nombre):
        registros = self.cargar_usuarios()
        registros = [r for r in registros if r["nombre"] != nombre]
        self._guardar_csv(registros)
        
    #carga los usuarios desde el csv, filtra por nombre y aumenta asistencia en 1, guarda el archivo nuevamente.
    def registrar_asistencia(self, nombre):
        registros = self.cargar_usuarios()
        for r in registros:
            if r["nombre"] == nombre:
                r["asistencias"] = str(int(r.get("asistencias", 0)) + 1)
                break
        self._guardar_csv(registros)