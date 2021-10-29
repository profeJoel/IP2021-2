import math

def angulo(a, b):
    if a <= 0 or b <= 0:
        print("Error, Los valores debe ser positivos")
        bac = 0
    else:
        c = math.sqrt(a**2 + b**2)
        bac = math.asin(a/c)
    
    return bac

# equivalente a la función main
if __name__ == "__main__":
    print("Ingrese el valor del cateto a: ")
    cateto_a = float(input())
    print("Ingrese el valor del cateto b: ")
    cateto_b = float(input())

    BAC = angulo(cateto_a, cateto_b)

    print("El valor del angulo del triangulo es: " + str(BAC))