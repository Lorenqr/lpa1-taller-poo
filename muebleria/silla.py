# muebleria/silla.py
from .mueble import Mueble

class Silla(Mueble):
    def __init__(self, material, precio, tiene_respaldo):
        super().__init__(material, precio)
        self.tiene_respaldo = tiene_respaldo

    def calcular_precio_final(self):
        return self.precio * 1.1 if self.tiene_respaldo else self.precio