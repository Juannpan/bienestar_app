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

