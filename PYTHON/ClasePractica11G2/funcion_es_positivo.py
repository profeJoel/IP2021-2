def es_positivo(numero):
    respuesta = numero > 0
    return respuesta

if __name__ == "__main__":
    print("Ingrese un número: ")
    numero = int(input())

    #print("El resultado es: " + str(es_positivo(numero)))

    if es_positivo(numero):
        print("El número es Positivo")
    else:
        print("El Número es Negativo")