def alcanza_limite(planta):
    return planta >= 10000

if __name__ == "__main__":

    planta1 = 0
    planta2 = 0
    planta3 = 0
    productorasPlanta1 = 0
    productorasPlanta2 = 0
    productorasPlanta3 = 0
    primeraVezPlanta1 = True
    primeraVezPlanta2 = True
    primeraVezPlanta3 = True

    print("Bienvenidos a Industrias NOLUC")
    
    while not alcanza_limite(planta1) or not alcanza_limite(planta2) or not alcanza_limite(planta3):
        print("Ingrese la cantidad de leche de la familia productora")
        cantidadLeche = float(input())
        while cantidadLeche <= 0:
            print("Ingrese la cantidad de leche de la familia productora")
            cantidadLeche = float(input())

        if not alcanza_limite(planta1):
            planta1 += cantidadLeche
            productorasPlanta1 += 1

        elif not alcanza_limite(planta2):
            planta2 += cantidadLeche
            productorasPlanta2 += 1
        else:
            planta3 += cantidadLeche
            productorasPlanta3 += 1

        if alcanza_limite(planta1) and primeraVezPlanta1:
            print("Planta 1 alcanza su límite de producción")
            primeraVezPlanta1 = False
        
        if alcanza_limite(planta2) and primeraVezPlanta2:
            print("Planta 2 alcanza su límite de producción")
            primeraVezPlanta2 = False
        
        if alcanza_limite(planta3) and primeraVezPlanta3:
            print("Planta 3 alcanza su límite de producción")
            primeraVezPlanta3 = False

    print("Se alcanzó el límite de producción diario en todas las plantas de procesamiento")
    print("Planta 1: \n - Total de Producción: " + str(planta1) + "\n - Cantidad de Productore: " + str(productorasPlanta1))
    print("Planta 2: \n - Total de Producción: " + str(planta2) + "\n - Cantidad de Productore: " + str(productorasPlanta2))
    print("Planta 3: \n - Total de Producción: " + str(planta3) + "\n - Cantidad de Productore: " + str(productorasPlanta3))
