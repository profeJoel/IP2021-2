suma = 0
numeros = [None] * 8

for i in range(8):
    print("Ingrese el " + str(i+1) + "° valor: ")
    numeros[i] = int(input())

    suma = suma + numeros[i]

print("El total de la suma es: " + str(suma))