import pytest
from juego import numero_aleatorio, comparar_suposicion

# Prueba para la función numero_aleatorio
def test_numero_aleatorio():
    numero = numero_aleatorio()
    assert isinstance(numero, int)
    assert 1 <= numero <= 100

# Pruebas para la función comparar_suposicion
@pytest.mark.parametrize("numero_secreto, suposicion, expected_result",
                         [(50, 50, "acertaste"),  # Acierto
                          (50, 60, "menor"),      # Suposición mayor
                          (50, 40, "mayor")])    # Suposición menor
def test_comparar_suposicion(numero_secreto, suposicion, expected_result):
    assert comparar_suposicion(numero_secreto, suposicion) == expected_result


