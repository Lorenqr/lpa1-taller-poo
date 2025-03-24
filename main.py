# ejecutar el programa y probar las clases

from rich.console import Console
from rich.table import Table
from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario
from muebleria.inventario import Inventario

console = Console()

silla = Silla("madera", 50.0, "rimax")
mesa = Mesa("vidrio", 120.0)
armario = Armario("metal", 300.0)

# Crear una tabla para mostrar la información
table = Table(title="Información de Muebles", show_header=True, header_style="white")
table.add_column("Mueble", style="cyan")
table.add_column("Material", style="green")
table.add_column("Precio Base", style="yellow")
table.add_column("Precio Final", style="bold red")

# Agregar filas a la tabla
table.add_row("Silla", silla.material, f"${silla.precio:.2f}", f"${silla.calcular_precio_final():.2f}", style="cyan")
table.add_row("Mesa", mesa.material, f"${mesa.precio:.2f}", f"${mesa.calcular_precio_final():.2f}", style="bold red")
table.add_row("Armario", armario.material, f"${armario.precio:.2f}", f"${armario.calcular_precio_final():.2f}", style="hot_pink")

# Mostrar la tabla
console.print(table)

#control de inventario
console.print("Se agregaran los materiales al inventario")
inventario = Inventario()
inventario.agregar_mueble(silla)
inventario.agregar_mueble(mesa)
inventario.agregar_mueble(armario)

console.print("Mostrar los materiales agregados")
inventario.mostrar_inventario()

console.print("Se elimina materiales para armario")
inventario.eliminar_mueble(armario)

console.print("Mostrar los materiales existentes")
inventario.mostrar_inventario()

#Serializador de json
json_silla = silla.to_json()
print("Silla serializada a JSON")
print(json_silla)
