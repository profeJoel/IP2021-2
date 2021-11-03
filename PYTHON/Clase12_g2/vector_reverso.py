if __name__ == "__main__":
    print("Ingrese el tamaño del vector")
    n = int(input())
    while n <= 0:
        print("Ingrese el tamaño del vector")
        n = int(input())

    v = [None] * n # Creando un vector con n posiciones

    for i in range(n): # i = [0,...,n-1]
        print("Ingrese los valores del vector")
        v[i] = int(input())

    print("Mostrar el vector al reverso")

    for i in range(n):
        print(str(v[n-1-i]))