
import argparse
from .inventario import Inventario
from .silla import Silla
from .mesa import Mesa
from .armario import Armario

def main():
    parser = argparse.ArgumentParser(description="Gestión de Mueblería")
    parser.add_argument("--agregar", type=str, help="Agregar un mueble")
    args = parser.parse_args()

    inventario = Inventario()
    if args.agregar:
        inventario.agregar_mueble(Silla("madera", 50.0, True))
        print("Mueble agregado al inventario.")

if __name__ == "__main__":
    main()