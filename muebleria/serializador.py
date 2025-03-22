import json

def serializar(mueble):
    return json.dumps(mueble.__dict__)

def deserializar(cls, data):
    return cls(**json.loads(data))