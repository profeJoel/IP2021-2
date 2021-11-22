if __name__ == "__main__":
    M = [None] * 5
    for fila in range(5):
        M[fila] = [None] * 5

    for i in range(5):
        for j in range(5):
            if j==0 or j==4:
                M[i][j] = 'm'
            elif i==j and i<3:
                M[i][j] = 'm'
            elif i+j==4 and i<3:
                M[i][j] = 'm'
            else:
                M[i][j] = ' '

    """
    for i in range(5):
        for j in range(5):
            print(M[i][j], end=" ")
        print(" ")
    """
    archivo = open("letraM.txt","a")
    for i in range(5):
        for j in range(5):
            archivo.write(M[i][j]+" ")
        archivo.write("\n")