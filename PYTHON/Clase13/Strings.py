def contar_letras(texto):
    return len(texto)

if __name__ == "__main__":
    print("Ingrese una palabra: ")
    palabra1 = input()
    print("Ingrese una palabra: ")
    palabra2 = input()

    # print("La cantidad de letras de esta palabra son: " + str(contar_letras(palabra)))

    if contar_letras(palabra1) > contar_letras(palabra2):
        print("Palabra: " + palabra1 + " es más larga con " + str(contar_letras(palabra1)))
    elif contar_letras(palabra1) == contar_letras(palabra2):
        print("Las palabras: " + palabra1 + " y " + palabra2 + " tienen igual largo, con " + str(contar_letras(palabra2)))
    else:
        print("Palabra: " + palabra2 + " es más larga con " + str(contar_letras(palabra2)))