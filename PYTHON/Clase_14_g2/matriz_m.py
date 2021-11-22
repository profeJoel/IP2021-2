if __name__ == "__main__":
    M = [None] * 5
    for fila in range(5):
        M[fila] = [None] * 5

    for f in range(5):
        for c in range(5):
            if c==0 or c==4:
                M[f][c] = 'm'
            elif f==1 and (c==1 or c==3):
                M[f][c] = 'm'
            elif f==2 and c==2:
                M[f][c] = 'm'
            else:
                M[f][c] = ' '

    """
    print("La matriz M es:\n ")
    
    for f in range(5):
        for c in range(5):
            print(M[f][c], end=" ")
        print(" ")
    """

    archivo = open("letraM.txt", "a") # se crea un archivo y se escribe al final
    for f in range(5):
        for c in range(5):
            archivo.write(M[f][c] + " ")
        archivo.write("\n")


    