if __name__ == "__main__":
    # Carga y lectura del archivo csv
    delitos = open("delitos_puerto_montt.csv", "r")

    hurtos_300 = open("hurtos_300_puerto_montt.csv", "a") # Creación de archivo de salida

    # Identificar las líneas que tienen más de 300 hurtos
    primero = True # para saltarse la primer línea
    for delito in delitos:
        if primero:
            primero = False
        else:
            valor = delito.split(',')
            hurto = int(valor[2])
            if hurto > 300:
                #print(delito)
                hurtos_300.write(delito) # se añade el delito con >300 hurtos