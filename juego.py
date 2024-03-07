import random
from colorama import init, Fore, Style

# Inicializar colorama 
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

def suposicion_computadora(rango_inferior, rango_superior):
    """Genera una suposición basada en el rango proporcionado."""
    return random.randint(rango_inferior, rango_superior)

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

        # Definir el rango inicial para la suposición de la computadora
        rango_inferior = 1
        rango_superior = 100

        while True:
            # Turno del jugador
            intento = solicitar_suposicion(nombre)
            intentos += 1
            suposiciones.append(intento)

            resultado = comparar_suposicion(numero_secreto, intento)
            if resultado == "acertaste":
                print(Style.BRIGHT + Fore.GREEN + f"¡Felicidades, {nombre}! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
                print("Suposiciones realizadas:", suposiciones)
                break
            elif resultado == "mayor":
                print(Fore.RED + f"{nombre}, el número secreto es mayor.")
                # La computadora ajusta su rango superior
                rango_superior = intento - 1
            else:
                print(Fore.RED + f"{nombre}, el número secreto es menor.")
                # La computadora ajusta su rango inferior
                rango_inferior = intento + 1

            # Verificar y ajustar el rango para la suposición de la computadora
            if rango_superior < rango_inferior:
                # Si el rango superior es menor que el rango inferior, invierte los rangos
                rango_inferior, rango_superior = rango_superior, rango_inferior

            # Turno de la computadora
            suposicion_pc = suposicion_computadora(rango_inferior, rango_superior)
            print(Fore.BLUE + f"La computadora supone que el número es: {suposicion_pc}")

            resultado_pc = comparar_suposicion(numero_secreto, suposicion_pc)
            if resultado_pc == "acertaste":
                print(Style.BRIGHT + Fore.GREEN + f"¡La computadora ha adivinado el número secreto {numero_secreto} en {intentos} intentos!")
                break
            elif resultado_pc == "mayor":
                print(Fore.RED + "Computadora el número secreto es mayor.")
                # La computadora ajusta su rango inferior
                rango_inferior = suposicion_pc + 1
            else:
                print(Fore.RED + "Computadora el número secreto es menor.")
                # La computadora ajusta su rango superior
                rango_superior = suposicion_pc - 1

        if not jugar_nuevo():
            print(Fore.CYAN + "Gracias por jugar. ¡Hasta luego, " + nombre + "!")
            break

if __name__ == "__main__":
    jugar()
