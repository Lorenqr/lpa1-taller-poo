class Inventario:
    def __init__(self):
        self.muebles = []

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)
        print("Se agrego el material correctamente")
        
    def eliminar_mueble(self, mueble):
        if mueble in self.muebles:
            self.muebles.remove(mueble)
            print("Material eliminado")
        else:
            print("No existe el mueble en el inventario")

    def mostrar_inventario(self):
        if not self.muebles:
            print("No existe materiales")
        else:
            for mueble in self.muebles:
                print(mueble.mostrar_nombre())