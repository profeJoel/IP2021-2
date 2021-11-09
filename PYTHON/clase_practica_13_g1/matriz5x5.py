if __name__ == "__main__":
    M = [None] * 5
    for fila in range(5):
        M[fila] = [None] * 5

    for x in range(5):
        for y in range(5):
            if x == y:
                M[x][y] = 0
            elif x+y == 4:
                M[x][y] = 0
            else:
                M[x][y] = 1

    # imprimir matriz

    for x in range(5):
        for y in range(5):
            print(str(M[x][y]), end=" ")
        print(" ")