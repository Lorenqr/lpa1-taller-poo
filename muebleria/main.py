# ejecutar el programa y probar las clases

from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

silla = silla("madera", 50.0, True)
mesa = Mesa("vidrio", 120.0, "redonda")
armario = Armario("metal", 300.0, 4)

print(Silla)
print(f"Precio final de la silla: ${silla.calcular_precio_final():.2f}")

print(mesa)
print(f"Precio final de la mesa: ${mesa.calcular_precio_final():.2f}")

print(armario)
print(f"Precio final del armario: ${armario.calcular_precio_final():.2f}")