if __name__ == "__main__":
    filas = 4
    columnas = 3
    suma = 0

    M = [None] * filas
    for fila in range(filas):
        M[fila] = [None] * columnas

    for fila in range(filas):
        for columna in range(columnas):
            print("Ingrese un valor [" + str(fila) + ","+str(columna) + "]: ")
            M[fila][columna] = int(input())

    print("La matriz M es:")
    
    for fila in range(filas):
        for columna in range(columnas):
            print(str(M[fila][columna]),end=" ")
        print(" ")

    # Suma de la matriz
    
    for fila in range(filas):
        for columna in range(columnas):
            suma += M[fila][columna]

    print("La suma es: " + str(suma))