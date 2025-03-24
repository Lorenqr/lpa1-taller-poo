# clases relacionadas con los muebles

from abc import ABC, abstractmethod
import json

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
        
    def mostrar_nombre(self):
        return self.material
    
    def to_dict(self):
        return{
            'material': self.material,
            'precio': self.precio
        }
    
    def to_json_(self):
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['material'], data['precio'])
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls.from_dict(data)
    
    