def calcular_area_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        print("Error, los valore deben ser positivos")
        return 0

    else:
        area = base * altura
        return area


if __name__ == "__main__":
    print("Ingrese el valor de la base: ")
    base = float(input())
    print("Ingrese el valor de la altura: ")
    altura = float(input())

    print("El área del rectángulo es: " + str(calcular_area_rectangulo(base,altura)))
    