import random
from colorama import init, Fore, Style

# Inicializar colorama (esto es necesario en Windows)
init()

def numero_aleatorio():
    """Genera un número aleatorio entre 1 y 100."""
    return random.randint(1, 100)

def mostrar_mensaje_bienvenida(nombre):
    """Muestra un mensaje de bienvenida al inicio del juego."""
    print(Fore.CYAN + f"Bienvenido al juego adivina el número, {nombre}!")

def solicitar_suposicion(nombre):
    """Solicita al jugador que ingrese su suposición."""
    return int(input(f"{nombre}, ingresa tu suposición: "))

def comparar_suposicion(numero_secreto, suposicion):
    """Compara la suposición del jugador con el número secreto."""
    if suposicion == numero_secreto:
        return "acertaste"
    elif suposicion < numero_secreto:
        return "mayor"
    else:
        return "menor"

def jugar_nuevo():
    """Pregunta al jugador si quiere jugar de nuevo."""
    return input("¿Quieres jugar de nuevo? (s/n): ").lower() == 's'

def jugar():
    """Función principal para jugar al juego de adivinar el número."""
    nombre = input("Por favor, ingresa tu nombre: ")
    mostrar_mensaje_bienvenida(nombre)

    while True:
        numero_secreto = numero_aleatorio()
        intentos = 0
        suposiciones = []

        print(Fore.YELLOW + "He pensado en un número entre 1 y 100. ¡Adivina!")

        while True:
            intento = solicitar_suposicion(nombre)
            intentos += 1
            suposiciones.append(intento)

            resultado = comparar_suposicion(numero_secreto, intento)
            if resultado == "acertaste":
                print(Style.BRIGHT + Fore.GREEN + f"¡Felicidades, {nombre}! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
                print("Suposiciones realizadas:", suposiciones)
                break
            elif resultado == "mayor":
                print(Fore.RED + "El número secreto es mayor.")
            else:
                print(Fore.RED + "El número secreto es menor.")

        if not jugar_nuevo():
            print(Fore.CYAN + "Gracias por jugar. ¡Hasta luego, " + nombre + "!")
            break

if __name__ == "__main__":
    jugar()

