import os

if __name__ == "__main__":
    # Creación de un archivo
    """
    print("Vamos a Crear un Archivo")
    open("nuevo_archivo.txt","x")
    print("Archivo Creado!!!")
    """

    # Leer un archivo
    """
    print("Vamos a leer un archivo")
    archivo = open("nuevo_archivo.txt", "r")
    """

    # Lee todo el texto del archivo
    # print("El texto en el archivo es: \n" + archivo.read())

    # Lee hasta la cantidad de caracteres que se le indique
    # print("El texto en el archivo es: \n" + archivo.read(10))

    # Lee por linea
    # print("El texto en el archivo es: \n" + archivo.readline())

    # Lee cada linea del archivo , linea es una variable y archivo es un objeto iterable
    """
    for linea in archivo:
        print(linea)
    """

    #Escribir al final del texto
    """
    print("Vamos a añadir más texto al archivo")
    archivo = open("nuevo_archivo.txt", "a")
    nuevo_texto = "\nEste es una nueva linea añadida al final"
    archivo.write(nuevo_texto)
    """

    # Sobrescribir archivo
    """
    print("Vamos a sobrescribir el archivo")
    archivo = open("nuevo_archivo.txt", "w")
    nuevo_texto = "\nEste es una nueva linea que sobrescribe la anterior"
    archivo.write(nuevo_texto)
    """


    #archivo.close()

    # Eliminar el archivo
    """
    print("Vamos a eliminar un archivo")
    os.remove("nuevo_archivo.txt")
    print("Archivo Eliminado")
    """

