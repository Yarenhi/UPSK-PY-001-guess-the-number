import random  # Importamos el módulo random para generar números aleatorios

def numero_aleatorio():  # Definimos una función para generar un número aleatorio entre 1 y 100
    return random.randint(1, 100)  # Utilizamos la función randint() de random para obtener un número aleatorio

def jugar():  # Definimos la función principal para jugar
    numero_secreto = numero_aleatorio()  # Generamos el número secreto llamando a la función numero_aleatorio()
    intentos = 0  # Inicializamos el contador de intentos en 0

    while True:  # Comenzamos un bucle infinito para solicitar a la jugadora que adivine el número
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))  # Solicitamos un intento a la jugadora y lo convertimos a entero
        intentos += 1  # Incrementamos el contador de intentos en cada iteración

        if intento == numero_secreto:  # Comparamos el intento con el número secreto
            print(f"Felicidades, has adivinado el número secreto {numero_secreto} en {intentos} intentos!")  # Imprimimos un mensaje de felicitaciones si el intento es correcto
            break  # Salimos del bucle
        elif intento < numero_secreto:  # Si el intento es menor que el número secreto
            print("El número secreto es mayor.")  # Imprimimos un mensaje indicando que el número secreto es mayor
        else:  # Si el intento es mayor que el número secreto
            print("El número secreto es menor.")  # Imprimimos un mensaje indicando que el número secreto es menor

if __name__ == "__main__":  # Verificamos si el script se está ejecutando directamente
    jugar()  # Llamamos a la función jugar() para iniciar el juego

