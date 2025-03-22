# muebleria/mesa.py
from .mueble import Mueble

class Mesa(Mueble):
    def __init__(self, material, precio, forma):
        super().__init__(material, precio)
        self.forma = forma

    def calcular_precio_final(self):
        return self.precio * 1.2 if self.forma == "redonda" else self.precio