if __name__ == "__main__":
    opcion = 1
    n = 1

    print("Bienvenido al registro de estudiantes!")

    archivo = open("listado.csv", "a")
    archivo.write("N, NOMBRE, EDAD \n")

    while opcion == 1:
        print("Ingrese el nombre del estudiante: ")
        nombre = input()
        print("Ingrese la edad del estudiante: ")
        edad = int(input())
        while edad < 0 or edad > 121:
            print("Ingrese la edad del estudiante: ")
            edad = int(input())
        
        archivo.write(str(n) + ", " + nombre + ", " + str(edad) + "\n")
        n += 1

        print("Desea ingresar un nuevo Usuario?\nMarque (1) para seguir o (0) para salir...")
        opcion = int(input())
        while opcion < 0 or opcion > 1:
            print("Desea ingresar un nuevo Usuario?\nMarque (1) para seguir o (0) para salir...")
            opcion = int(input())

    archivo.close()
