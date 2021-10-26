import math

def calcular_angulo_triangulo(a,b):
    if a <= 0 or b <= 0:
        print("Error, los valores deben ser positivos")
        return 0

    else:
        c = math.sqrt(a**2+b**2)
        angulo = math.asin(a/c)
        return angulo

if __name__ == "__main__":
    print("Ingrese el valor de a: ")
    a = float(input()) 
    print("Ingrese el valor de b: ")
    b = float(input())

    angulo = calcular_angulo_triangulo(a,b)
    print("El angulo buscado es: " + str(angulo))