# ejecutar el programa y probar las clases

from rich.console import Console
from rich.table import Table
from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

console = Console()

silla = Silla("madera", 50.0, True)
mesa = Mesa("vidrio", 120.0, "redonda")
armario = Armario("metal", 300.0, 4)

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