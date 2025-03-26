
import argparse
from muebleria.silla import Silla
from muebleria.inventario import Inventario
import json

inventario = Inventario()

def agregar_mueble(args):
    if args.precio <= 0:
        print("Error: El precio debe ser positivo.")
        return
    silla = Silla(args.material, args.precio, args.tipo)
    inventario.agregar_mueble(silla)
    print(f"Silla agregada: Material={args.material}, Precio=${args.precio}")

def eliminar_mueble(args):
    for mueble in inventario.muebles:
        if mueble.material == args.material:
            inventario.eliminar_mueble(mueble)
            print(f"Mueble con material {args.material} eliminado.")
            return
    print("No se encontró el mueble.")

def listar_muebles(args=None):
    inventario.mostrar_inventario()

def guardar_inventario(args):
    with open(args.archivo, 'w') as file:
        muebles_json = [mueble.to_dict() for mueble in inventario.muebles]
        json.dump(muebles_json, file, indent=4)
    print(f"Inventario guardado en {args.archivo}")

def cargar_inventario(args):
    try:
        with open(args.archivo, 'r') as file:
            try:
                muebles_json = json.load(file)
                inventario.muebles.clear()
                for mueble_data in muebles_json:
                    silla = Silla.from_dict(mueble_data)
                    inventario.agregar_mueble(silla)
                print(f"Inventario cargado desde {args.archivo}")
            except json.JSONDecodeError:
                print("Error: El archivo no es un JSON válido.")
    except FileNotFoundError:
        print(f"Error: El archivo {args.archivo} no existe.")

def main():
    parser = argparse.ArgumentParser(description="Sistema de Gestión de Mueblería")
    subparsers = parser.add_subparsers()

    # Comando 'agregar'
    parser_agregar = subparsers.add_parser('agregar', help='Agrega una silla al inventario')
    parser_agregar.add_argument('material', help='Material de la silla (ej: madera, metal)')
    parser_agregar.add_argument('precio', type=float, help='Precio (debe ser > 0)')
    parser_agregar.add_argument('tipo', help='Tipo de silla (ej: oficina, ergonómica)')
    parser_agregar.set_defaults(func=agregar_mueble)

    # Comando 'eliminar'
    parser_eliminar = subparsers.add_parser('eliminar', help='Elimina un mueble por material')
    parser_eliminar.add_argument('material', help='Material del mueble a eliminar')
    parser_eliminar.set_defaults(func=eliminar_mueble)

    # Comando 'listar'
    parser_listar = subparsers.add_parser('listar', help='Muestra el inventario actual')
    parser_listar.set_defaults(func=listar_muebles)

    # Comando 'guardar'
    parser_guardar = subparsers.add_parser('guardar', help='Guarda el inventario en JSON')
    parser_guardar.add_argument('archivo', help='Ruta del archivo de salida (ej: inventario.json)')
    parser_guardar.set_defaults(func=guardar_inventario)

    # Comando 'cargar'
    parser_cargar = subparsers.add_parser('cargar', help='Carga el inventario desde JSON')
    parser_cargar.add_argument('archivo', help='Ruta del archivo a cargar (ej: inventario.json)')
    parser_cargar.set_defaults(func=cargar_inventario)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()