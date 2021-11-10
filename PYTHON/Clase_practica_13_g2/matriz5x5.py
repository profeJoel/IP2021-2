if __name__ == "__main__":
    M = [None] * 5
    for fila in range(5):
        M[fila] = [None] * 5

    for f in range(5):
        for c in range(5):
            #consultar la diagonal principal
            if f == c:
                M[f][c] = 0
            #Consultar la diagonal secundaria
            elif f + c == 4:
                M[f][c] = 0
            else:
                M[f][c] = 1

    print(" La matriz es: ")

    for f in range(5):
        for c in range(5):
            print(M[f][c], end=" ")
        print(" ")