# pruebas unitarias utilizando pytest

from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

def test_silla_precio_final():
    silla = Silla("madera", 50.0, "banco")
    assert silla.calcular_precio_final() == 50.0

def test_mesa_precio_final():
    mesa = Mesa("vidrio", 120.0)
    assert not mesa.calcular_precio_final() == 144.0

def test_armario_precio_final():
    armario = Armario("metal", 300.0)
    assert armario.calcular_precio_final() != 360.0