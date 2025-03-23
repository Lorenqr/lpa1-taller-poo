# muebleria/mesa.py
from .mueble import Mueble

class Mesa(Mueble):
    def __init__(self, material, precio):
        super().__init__(material, precio)

    def calcular_precio_final(self):
        return self.precio