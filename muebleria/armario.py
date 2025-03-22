# muebleria/armario.py
from .mueble import Mueble

class Armario(Mueble):
    def __init__(self, material, precio, num_puertas):
        super().__init__(material, precio)
        self.num_puertas = num_puertas

    def calcular_precio_final(self):
        return self.precio * (1 + 0.05 * self.num_puertas)