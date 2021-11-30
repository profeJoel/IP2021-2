import os

def guardarPartida(jugador1, jugador2, resultado):
    partidas = open("resultado_gato.txt", "a")
    partidas.write("Jugadores: [" + jugador1 + "] y [" +jugador2+"] > Resultado: " + resultado + "\n")

def ver_resultados():
    partidas = open("resultado_gato.txt", "r")
    os.system('cls')
    print("\nResultados de Partidas Pasadas")
    for partida in partidas:
        print(partida)

def imprimir_matriz(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == None:
                print("[ ]", end= " ")
            else:           
                print("[" + matriz[i][j] + "]", end=" ")
        print(" ")

def gana_partida(matriz, nombre, simbolo):
    if matriz[0][0] == simbolo and matriz[0][1] == simbolo and matriz[0][2] == simbolo:
        return True
    if matriz[1][0] == simbolo and matriz[1][1] == simbolo and matriz[1][2] == simbolo:
        return True
    if matriz[2][0] == simbolo and matriz[2][1] == simbolo and matriz[2][2] == simbolo:
        return True
        
    if matriz[0][0] == simbolo and matriz[1][0] == simbolo and matriz[2][0] == simbolo:
        return True
    if matriz[0][1] == simbolo and matriz[1][1] == simbolo and matriz[2][1] == simbolo:
        return True
    if matriz[0][2] == simbolo and matriz[1][2] == simbolo and matriz[2][2] == simbolo:
        return True

    if matriz[0][0] == simbolo and matriz[1][1] == simbolo and matriz[2][2] == simbolo:
        return True
    if matriz[0][2] == simbolo and matriz[1][1] == simbolo and matriz[2][0] == simbolo:
        return True

    return False

def tomar_turno(matriz, nombre, nombre2, simbolo):
    print("Es turno del jugador: " + nombre)
    print("Ingrese las coordenadas de la matriz donde quiere jugar:")
    print("Ingrese fila [0,2]:")
    fila = int(input())
    while fila<0 or fila>2:
        print("Ingrese fila [0,2]:")
        fila = int(input())
    print("Ingrese columna [0,2]:")
    columna = int(input())
    while columna<0 or columna>2:
        print("Ingrese columna [0,2]:")
        columna = int(input())
    
    while matriz[fila][columna] != None:
        print("Error, Coordenadas ya ocupadas, Ingrese nuevas coordenadas de la matriz donde quiere jugar:")
        print("Ingrese fila [0,2]:")
        fila = int(input())
        while fila<0 or fila>2:
            print("Ingrese fila [0,2]:")
            fila = int(input())
        print("Ingrese columna [0,2]:")
        columna = int(input())
        while columna<0 or columna>2:
            print("Ingrese columna [0,2]:")
            columna = int(input())

    matriz[fila][columna] = simbolo

    if gana_partida(matriz, nombre, simbolo):
        print("Jugador: " + nombre + " es el GANADOR de la Partida")
        guardarPartida(nombre,nombre2,"Gana Jugador: "+nombre)
        exit()

if __name__ == "__main__":
    simbolos_aceptados = ['O','X']
    tablero = [None] * 3
    for i in range(3):
        tablero[i] = [None] * 3

    print("\nBienvenido al Juego del Gato")

    print("\nOpciones: \n 1- Nueva Partida \n 2- Ver Resultados Partidas anteriores")
    opcion = int(input())
    while opcion <1 or opcion>2:
        print("\nOpciones: \n 1- Nueva Partida \n 2- Ver Resultados Partidas anteriores")
        opcion = int(input())

    if opcion == 1:
        print("\n\nIndique el nombre del Jugador 1: ")
        jugador1 = input()
        print("Indique cual simbolo ocupará el jugador 1: ")
        simbolo_j1 = input()
        while not simbolo_j1 in simbolos_aceptados:
            print("Indique cual simbolo ocupará el jugador 1: ")
            simbolo_j1 = input()

        print("\n\nIndique el nombre del Jugador 2: ")
        jugador2 = input()
        print("Indique cual simbolo ocupará el jugador 2: ")
        simbolo_j2 = input()
        while not simbolo_j2 in simbolos_aceptados or simbolo_j2 == simbolo_j1:
            print("Indique cual simbolo ocupará el jugador 2: ")
            simbolo_j2 = input()
        
        os.system('cls')

        print("\npartida Iniciada")

        turno_jugador1 = [0,2,4,6,8]
        turno_jugador2 = [1,3,5,7]

        for turno in range(9):
            os.system('cls')
            print("Turno: " + str(turno))
            imprimir_matriz(tablero)

            if turno in turno_jugador1:
                tomar_turno(tablero, jugador1, jugador2, simbolo_j1)
            else:
                tomar_turno(tablero, jugador2, jugador1, simbolo_j2)

        os.system('cls')
        print("Turno: " + str(turno))
        imprimir_matriz(tablero)
        print("\nSe terminaron todos los turnos disponibles, se determina que es un EMPATE")
        guardarPartida(jugador1, jugador2, "EMPATE")

    else:
        ver_resultados()