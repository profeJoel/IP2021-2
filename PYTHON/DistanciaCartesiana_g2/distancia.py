import math

print("Ingrese el primer punto cartesiano")
x1 = float(input())
y1 = float(input())
print("El punto ingresado es (" + str(x1) + "," + str(y1) + ")")

print("Ingrese el segundo punto cartesiano")
x2 = float(input())
y2 = float(input())
print("El punto ingresado es (" + str(x2) + "," + str(y2) + ")")

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("La distancia cantesiana es: " + str(d))