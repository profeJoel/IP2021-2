import os
import random

def mostrar(sujeto):
    for i in range(4):
        for j in range(6):
            print(sujeto[i][j],end='')
        print('')

def crear_palabra_oculta(palabra):
    palabra = palabra.upper()
    total = len(palabra)
    posicion_aleatoria = random.randint(0,total-1)
    if total >= 5:
        nueva_posicion = random.randint(0,total-1)
        while nueva_posicion <= posicion_aleatoria:
            nueva_posicion = random.randint(0,total-1)

    print("posicion aleatoria: " + str(posicion_aleatoria))
    nueva_palabra = "" # mantener el largo de la palabra
    for i in range(total):
        if i == posicion_aleatoria:
            nueva_palabra += palabra[i]
            if total >= 5:
                posicion_aleatoria = nueva_posicion
        else:
            nueva_palabra += '_'
    
    return nueva_palabra

def eliminar_miembro(sujeto, intento):
    if intento == 5:
        sujeto[3][5] = ' '
    if intento == 4:
        sujeto[3][3] = ' '
        
    if intento == 3:
        sujeto[2][5] = ' '
    if intento == 2:
        sujeto[2][3] = ' '
        
    if intento == 1:
        sujeto[2][4] = ' '
        
    if intento == 0:
        sujeto[1][4] = ' '

def iniciar_partida(oculta, adivinar, sujeto):
    intentos = 6

    while intentos > 0:
        os.system('cls')
        print("Comienza la Partida, tiene " + str(intentos) + " intentos para identificar la palabra:")
        print("El estado del sujeto es:")
        mostrar(sujeto)
        print("La palabra a adivinar es: " + adivinar)
        print("\nOpciones de juego: \n 1- Adivinar letra \n 2- Adivinar palabra")
        opcion = int(input())
        while opcion <1 or opcion > 2:
            print("\nOpciones de juego: \n 1- Adivinar letra \n 2- Adivinar palabra")
            opcion = int(input())
        
        if opcion == 1:
            #Adivinar letra
            print("\nIngrese una Letra:")
            letra = input()
            while len(letra) > 1:
                print("\nIngrese una Letra:")
                letra = input()
            #preguntar si es que la letra esta en la palabra
            if letra in oculta:
                lugar = oculta.find(letra)
                adivinar = adivinar[:lugar] + letra.upper() + adivinar[lugar+1:]
            else:
                print("Error, la letra no está en la palabra")
                intentos -= 1
                eliminar_miembro(sujeto,intentos)
                
            #Identificar si el jugador ha ganado o no
            if adivinar == oculta:
                print("Eres el Ganador, La palabra si era: " + palabra)

        else:
            #ingresar la palabra
            print("Eres valiente, Ingresa la palabra: ")
            palabra = input()
            if palabra == oculta:
                print("\n\nEres el Ganador, La palabra si era: " + palabra)
                exit()
            else:
                intentos = 0
    
    os.system('cls')
    print("Partida Terminada:")
    print("El estado del sujeto es:")
    mostrar(sujeto)
    print("\n\nHas Perdido, La palabra era: " + oculta.upper())
    
        

if __name__ == "__main__":
    print("Bienvenidos al Juego del Ahorcado")

    """
    sujeto = [
        [' ', 'O', ' '],
        ['/', '|', '\\'],
        ['/', ' ', '\\']
    ]
    """

    sujeto = [
        [' ', '|', '-', '-', '|', ' '],
        [' ', '|', ' ', ' ', 'O', ' '],
        [' ', '|', ' ', '/', '|', '\\'],
        ['/', ' ', '\\','/', ' ', '\\']
    ]

    print("Ingrese la palabra secreta: ")
    palabra_oculta = input()
    palabra_adivinar = crear_palabra_oculta(palabra_oculta)

    os.system('cls')

    iniciar_partida(palabra_oculta, palabra_adivinar, sujeto)