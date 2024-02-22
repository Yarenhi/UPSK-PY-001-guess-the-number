import random
from colorama import init, Fore, Back, Style

# Inicializar colorama (esto es necesario en Windows)
init()


def numero_aleatorio():
    """Genera un número aleatorio entre 1 y 100."""
    return random.randint(1, 100)

def jugar():
    """Función principal para jugar al juego de adivinar el número."""
    print(Fore.MAGENTA +"¡Bienvenido al juego adivina el número!")

    while True:
        # Generamos un número secreto
        numero_secreto = numero_aleatorio()
        intentos = 0
        suposiciones = []  # Lista para almacenar las suposiciones de la jugadora

        print("He pensado en un número entre 1 y 100. ¡Adivina!")

        while True:
            # Solicitamos a la jugadora que adivine el número
            intento = int(input("Tu suposición: "))
            intentos += 1
            suposiciones.append(intento)  # Agregamos el intento a la lista de suposiciones

            # Comparamos el intento con el número secreto
            if intento == numero_secreto:
                print(Style.BRIGHT + f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
                print("Suposiciones realizadas:", suposiciones)  # Mostramos las suposiciones realizadas
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")

        # Preguntamos si la jugadora quiere jugar de nuevo
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    jugar()
