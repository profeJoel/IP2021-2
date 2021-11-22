if __name__ == "__main__":
    id = 1
    print("Bienvenido al programa de registro de estudiantes")
    opcion = 1

    archivo = open("lista_alumnos.csv", "a")
    archivo.write("N, NOMBRE, EDAD\n")

    while opcion == 1:
        print("Ingrese el nombre del estudiante:")
        nombre = input()
        print("Ingrese la edad del etudiante: ")
        edad = int(input())
        while edad <= 0 or edad >= 130:
            print("Ingrese la edad del etudiante: ")
            edad = int(input())
        
        archivo.write(str(id) + ", " + nombre + ", " + str(edad) + "\n")
        id += 1

        print("Desea ingresar otro estudiante? marque (1) para seguir o (0) para salir")
        opcion = int(input())
        while opcion<0 or opcion>1:
            print("Desea ingresar otro estudiante? marque (1) para seguir o (0) para salir")
            opcion = int(input())
