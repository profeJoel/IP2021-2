#Ejercicio 1
def mayor(a, b):
    if a > b:
        print(str(a) + " es mayor!!!")
        return a
    elif a < b:
        print(str(b) + " es mayor!!!")
        return b
    else:
        print(str(a) + " y " + str(b) + " Son iguales")
        return a

#Ejercicio 2
def menor(a, b):
    if a < b:
        print(str(a) + " es menor!!!")
        return a
    elif a > b:
        print(str(b) + " es menor!!!")
        return b
    else:
        print(str(a) + " y " + str(b) + " Son iguales")
        return a

#ejercicio 3
def potencia(a, b):
    p = 1
    es_neg = False # booleano:{False, True|}

    if b < 0:
        b = -b
        es_neg = True
    
    #range(b) = [0,1,...,b-1]
    for i in range(b):
        p *= a

    if es_neg:
        p = float(1/p)

    return p

if __name__ == "__main__":
    #Con una variable se almacena el retorno de la funcion
    valor_mayor = mayor(4,4)
    print("EL valor mayor es: " + str(valor_mayor))

    #Se muestra el valor, pero no se almacena
    print("El mayor valor es: " + str(mayor(3,5)))

    #Con una variable se almacena el retorno de la funcion
    valor_menor = menor(8,4)
    print("EL valor menor es: " + str(valor_menor))

    #Se muestra el valor, pero no se almacena
    print("El menor valor es: " + str(menor(3,5)))

    #Potencia
    #valor_potencia = potencia(2,9)
    valor_potencia = potencia(2,-2)
    print("El valor de la potencia es: " + str(valor_potencia))