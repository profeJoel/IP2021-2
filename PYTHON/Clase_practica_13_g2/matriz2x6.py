if __name__ == "__main__":
    M = [None] * 2
    for i in range(2):
        M[i] = [None] * 6

    par = 0
    impar = 0
    for i in range(2):
        for j in range(6):
            print("Ingrese el valor [" + str(i)+"]["+str(j)+"]:")
            M[i][j] = int(input())

            if M[i][j] % 2 == 0:
                par += 1
            else:
                impar += 1

    print("\nLa matriz es: ")

    for i in range(2):
        for j in range(6):
            print(M[i][j], end=" ")
        print(" ")

    print("\nLa cantidad de números Pares es: " + str(par))
    print("La cantidad de números Impares es: " + str(impar))