def area_rectangulo(b, a):
    if b <= 0 or a <= 0:
        print("Error, Los valores deben ser positivos")
        area = 0
    else:
        area = b * a
    
    return area

if __name__ == "__main__":
    print("Ingrese el valor de la Base:")
    b = float(input())
    print("Ingrese el valor de la Altura:")
    a = float(input())

    print("El área del rectángulo es: " + str(area_rectangulo(b, a)))
    