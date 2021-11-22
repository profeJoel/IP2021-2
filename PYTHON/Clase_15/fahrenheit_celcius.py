def fahr_a_cel(F):
    return (F-32)*5/9

if __name__ == "__main__":
    T_F = open("temp_f.csv","r")
    T_C = open("temp_c.csv","a") # creamos el nuevo archivo con valores celcius
    for linea in T_F: # estoy recorriendo cada línea del archivo en F
        palabra = linea.split(',')
        ciudad = palabra[0]
        fahr = int(palabra[1])
        celcius = fahr_a_cel(fahr)
        print("-> " + ciudad + ": " + str(celcius))
        T_C.write(ciudad + ", " + str(celcius) + "\n") # \n corresponde a un salto de línea

    T_F.close()
    T_C.close()