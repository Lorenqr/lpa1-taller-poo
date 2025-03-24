
import argparse
from muebleria.silla import Silla
from muebleria.inventario import Inventario
import json

inventario = Inventario()

def agregar_mueble(args):
    silla = Silla(args.material, args.precio, args.tipo)
    inventario.agregar_mueble(silla)
    
    
def eliminar_mueble(args):
    for mueble in inventario.muebles:
        if mueble.material() == args.material:
            inventario.eliminar_mueble(mueble)
            return
    print("No se encontro el mueble con ese material")
    
def listar_muebles(args):
    inventario.mostrar_inventario()
    
def guardar_inventario(args):
    with open(args.archivo, 'W') as file:
        muebles_json = [mueble.to_dict() for mueble in inventario.muebles]
        json.dump(muebles_json, file, indent=4)
    print(f"Inventario guardado en {args.archivo}")
    
def cargar_inventario(args):
    try:
        with open(args.archivo, 'r') as file:
            muebles_json = json.load(file)
            for mueble_data in muebles_json:
                silla = Silla.from_dict(mueble_data)
                inventario.agregar_mueble(silla)
        print(f"Inventario cargado desde {args.archivo}")
    except FileNotFoundError:
        print(f"El archivo {args.archivo} no existe.")
        
def main():
    parser = argparse.ArgumentParser(description="Gestión del inventario de la mueblería")

    # Subcomandos para diferentes acciones
    subparsers = parser.add_subparsers()

    # Subcomando para agregar un mueble
    parser_agregar = subparsers.add_parser('agregar', help='Agregar un mueble al inventario')
    parser_agregar.add_argument('material', help='Material del mueble')
    parser_agregar.add_argument('precio', type=float, help='Precio del mueble')
    parser_agregar.add_argument('tipo', help='Tipo de la silla (ej. ergonómica, oficina)')
    parser_agregar.set_defaults(func=agregar_mueble)

    # Subcomando para eliminar un mueble
    parser_eliminar = subparsers.add_parser('eliminar', help='Eliminar un mueble del inventario')
    parser_eliminar.add_argument('descripcion', help='Descripción completa del mueble a eliminar')
    parser_eliminar.set_defaults(func=eliminar_mueble)

    # Subcomando para listar los muebles
    parser_listar = subparsers.add_parser('listar', help='Listar todos los muebles en el inventario')
    parser_listar.set_defaults(func=listar_muebles)

    # Subcomando para guardar el inventario en un archivo JSON
    parser_guardar = subparsers.add_parser('guardar', help='Guardar el inventario en un archivo JSON')
    parser_guardar.add_argument('archivo', help='Archivo donde guardar el inventario')
    parser_guardar.set_defaults(func=guardar_inventario)

    # Subcomando para cargar el inventario desde un archivo JSON
    parser_cargar = subparsers.add_parser('cargar', help='Cargar el inventario desde un archivo JSON')
    parser_cargar.add_argument('archivo', help='Archivo desde el que cargar el inventario')
    parser_cargar.set_defaults(func=cargar_inventario)

    # Parseamos los argumentos y ejecutamos la función correspondiente
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()