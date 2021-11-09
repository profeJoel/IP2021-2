if __name__ == "__main__":
    par = 0
    impar = 0
    filas = 2
    columnas = 6

    M = [None] * filas
    for fila in range(filas):
        M[fila] = [None] * columnas

    for fila in range(filas):
        for columna in range(columnas):
            #LLenado de la matriz
            print("Ingrese el valor de [" + str(fila) + "][" + str(columna) + "]: ")
            M[fila][columna] = int(input())

            #Si es par o impar
            if M[fila][columna]%2 == 0:
                par += 1
            else:
                impar += 1

    #imprimir matriz

    for fila in range(filas):
        for columna in range(columnas):
            print(M[fila][columna], end= " ")
        print(" ")

    print("\nLa cantidad de números Pares es: " + str(par))
    print("La cantidad de números Impares es: " + str(impar))