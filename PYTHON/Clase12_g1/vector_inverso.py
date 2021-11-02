if __name__=="__main__":
    print("INgrese el tamaño del vector: ")
    n = int(input())
    while n<=0:
        print("INgrese el tamaño del vector: ")
        n = int(input())
    
    v = [None] * n #Creación de un vector de n posiciones de tipo None (sin tipo de datos asignado)

    for i in range(n):
        print("Ingrese un valor: ")
        v[i] = int(input())

    print("Muestra el vector inverso")

    for i in range(n):
        print(str(v[n-1-i]))