import unittest
from juego import numero_aleatorio, jugar

class TestGenerarNumeroSecreto(unittest.TestCase):
    def test_numero_aleatorio(self):
        # Probamos si la función numero_aleatorio genera números aleatorios dentro del rango esperado (entre 1 y 100)
        for _ in range(10):
            numero = numero_aleatorio()
            self.assertTrue(1 <= numero <= 100)

    # def test_jugar(self):
    #     # Probamos si la función jugar() se ejecuta sin errores
    #     try:
    #         jugar()
    #     except Exception as e:
    #         # Si se produce un error, la prueba falla y se imprime el mensaje de error
    #         self.fail(f"La función jugar() ha fallado con el siguiente error: {e}")

if __name__ == "__main__":
    unittest.main()
