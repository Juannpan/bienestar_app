import csv

class Usuario:
    def __init__(self, nombre, edad, actividad, clases, asistencias=0):
        self.nombre = nombre
        self.edad = int(edad)
        self.actividad = actividad
        self.clases = int(clases)
        self.asistencias = int(asistencias)
        self.valor_pagado = self.calcular_pago()

    def calcular_pago(self):
        precios = {
            "Spinning": 7000,
            "Fisioterapia": 10000,
            "Rumba": 5000,
            "Fortalecimiento": 6500
        }
        return precios.get(self.actividad, 0) * self.clases

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "actividad": self.actividad,
            "clases": self.clases,
            "valor_pagado": self.valor_pagado,
            "asistencias": self.asistencias
        }
class GestorUsuarios:
    def __init__(self, archivo="datos.csv"):
        self.archivo = archivo

    def cargar_usuarios(self):
        try:
            with open(self.archivo, mode="r", newline='', encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []

    def guardar_usuario(self, usuario: Usuario):
        registros = self.cargar_usuarios()
        registros.append(usuario.to_dict())
        self._guardar_csv(registros)
        
    def _guardar_csv(self, registros):
            with open(self.archivo, mode="w", newline='', encoding="utf-8") as f:
                fieldnames = ["nombre", "edad", "actividad", "clases", "valor_pagado", "asistencias"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(registros)