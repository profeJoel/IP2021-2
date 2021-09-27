print("Ingrese el diametro")
x = float(input())
while x <= 0:
    print("Ingrese el diametro")
    x = float(input())

pi = 3.14

perimetro = pi * x
area = (pi * x*x) /4

print(perimetro)
print(area)