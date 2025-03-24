# muebleria/armario.py
from muebleria.mueble import Mueble

class Armario(Mueble):
    def __init__(self, material, precio):
        super().__init__(material, precio)

    def calcular_precio_final(self):
        return self.precio
    
