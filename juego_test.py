import pytest
from juego import numero_aleatorio, comparar_suposicion, jugar

# Prueba para la función numero_aleatorio
def test_numero_aleatorio():
    # Generamos varios números aleatorios y verificamos que estén dentro del rango esperado
    for _ in range(100):
        numero = numero_aleatorio()
        assert 1 <= numero <= 100

# Pruebas para la función comparar_suposicion
@pytest.mark.parametrize("numero_secreto, suposicion, resultado_esperado", [
    (50, 40, "mayor"),  # Suposición menor que el número secreto
    (50, 60, "menor"),  # Suposición mayor que el número secreto
    (50, 50, "acertaste")  # Suposición igual al número secreto
])
def test_comparar_suposicion(numero_secreto, suposicion, resultado_esperado):
    resultado = comparar_suposicion(numero_secreto, suposicion)
    assert resultado == resultado_esperado

