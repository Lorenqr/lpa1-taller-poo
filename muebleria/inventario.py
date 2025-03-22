class Inventario:
    def __init__(self):
        self.muebles = []

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)

    def mostrar_inventario(self):
        for mueble in self.muebles:
            print(mueble)