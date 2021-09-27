print("Ingrese su edad")
edad = int(input())

if edad >= 0 and edad <= 130:
    if edad >= 18:
        print("Es Mayor de Edad")
    else:
        print("Es Menor de Edad")
else:
    print("Error: Valor edad no permitido")