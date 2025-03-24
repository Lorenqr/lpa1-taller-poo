from muebleria.mueble import Mueble
import json

class Silla(Mueble):
    def __init__(self, material, precio, tipo_silla):
        super().__init__(material, precio)
        self.tipo_silla = tipo_silla

    def calcular_precio_final(self):
        return self.precio
    
    def to_dict(self):
        data = super().to_dict()
        data['tipo_silla'] = self.tipo_silla
        return data
    
    @classmethod
    def from_dict(cls, data):
        mueble = super().from_dict(data)
        return cls(mueble.material, mueble.precio, data['tipo_silla'])
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls.from_dict(data)