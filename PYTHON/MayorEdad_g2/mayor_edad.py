print("Ingrese la edad")
edad = int(input()) # valor convertido a entero

if edad >= 0 and edad <= 130:
    if edad >= 18:
        print("Es Mayor de Edad")
    else:
        print("Es Menor de Edad")
else:
    print("ERROR: Valor Edad no Permitido")