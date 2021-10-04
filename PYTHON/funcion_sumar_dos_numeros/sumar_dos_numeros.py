x = 20 #Es una variable global

def sumar_dos_numeros(numero1, numero2):
    """
    resultado = numero1 + numero2
    return resultado
    """
    global x #se explicita la globalidad de la variable
    x = x + 1
    print("El resultado es " + str(x))
    return numero1 + numero2

if __name__ == "__main__":
    """
    resultado_suma_numeros = sumar_dos_numeros(1,2)
    print("El resultado es " + str(resultado_suma_numeros))
    """
    print("El resultado es " + str(x))
    print("El resultado es " + str(sumar_dos_numeros(1,2)))