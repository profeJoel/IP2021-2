datos = [None] * 3
for i in range(3):
    print("Ingrese el " + str(i+1) + "° valor: ")
    datos[i] = int(input())

print("\nValores Ingresados")
for i in range(3):
    print("datos["+str(i)+"] = " + str(datos[i]))