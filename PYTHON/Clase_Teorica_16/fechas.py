def contar_simbolo(fecha, simbolo):
    c = 0
    for letra in fecha:
        if letra == simbolo:
            c += 1
    return c

def verificar_formato(fecha, simbolo):
    return contar_simbolo(fecha,simbolo) == 2 and fecha[2] == simbolo and fecha[5] == simbolo

def dividir_fecha(fecha):
    if fecha[2] == '-':
        simbolo = '-'
    if fecha[2] == '/':
        simbolo = '/'

    elementos = fecha.split(simbolo)
    dd = int(elementos[0])
    mm = int(elementos[1])
    aaaa = int(elementos[2])

    return dd, mm, aaaa

def es_bisiesto(anho):
    return anho % 4 == 0 and anho % 100 == 0 and anho % 400 == 0

if __name__ == "__main__":

    print("Hola, Ingrese una fecha con el formato (dd-mm-aaaa) o (dd/mm/aaaa): ")
    fecha = input()

    if not (verificar_formato(fecha, "-") or verificar_formato(fecha, "/")):
        print("Error, el formato de la fecha no coincide con lo solicitado")
        exit()

    dia, mes, anho = dividir_fecha(fecha)

    if dia <= 0 or mes <= 0 or anho <= 0:
        print("Error, las fechas no pueden contener valores negativos o cero")
        exit()

    # validación de día
    meses_31 = [1,3,5,7,8,10,12]
    meses_30 = [4,6,9,11]
    if not((mes in meses_31 and dia <= 31) or (mes in meses_30 and dia <= 30) or (es_bisiesto(anho) and mes == 2 and dia <= 29) or (not(es_bisiesto(anho)) and mes == 2 and dia <= 28)):
        print("Error, Los días no corresponden a las fechas establecidas")
        exit()

    if mes > 12:
        print("Error, los meses corresponden desde 1 a 12 meses")
        exit()

    lista_mes = ["Mes","Enero","Febrero","Marzo","Abril","Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    # Termino del programa con validaciones correctas
    print("La fecha pasa todas las restricciones y corresponde a una fecha real en el formato establecido:")
    print("Es el día:" + str(dia) + " de " + lista_mes[mes] + " del año " + str(anho))
    