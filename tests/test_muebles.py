# pruebas unitarias utilizando pytest

from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

def test_silla():
    silla = Silla("madera", 50.0, True)
    assert silla.calcular_precio_final() == 55.0

def test_mesa():
    mesa = Mesa("vidrio", 120.0, "redonda")
    assert mesa.calcular_precio_final() == 144.0

def test_armario():
    armario = Armario("metal", 300.0, 4)
    assert armario.calcular_precio_final() == 360.0