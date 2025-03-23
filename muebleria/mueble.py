# clases relacionadas con los muebles

from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} -  Material: {self.material}, Precio: ${self.precio:.2f}"
    
    def aplicar_descuento(self, descuento):
        self.precio *= (1 - descuento / 100)