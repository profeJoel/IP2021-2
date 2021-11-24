import random

if __name__ == "__main__":
    huevos_desechados = 0
    huevos_retirados = 0

    desechados = []
    retirados = []

    #creación y llenado de matriz
    huevo = [None] * 5
    for f in range(5):
        huevo[f] = [None] * 6

    for i in range(5):
        for j in range(6):
            huevo[i][j] = random.randint(0,10)

    for i in range(5):
        for j in range(6):
            print(huevo[i][j], end=" ")
        print(" ")

    #Identificación de los casos de huevos desechados y retirados
    for i in range(5):
        for j in range(6):
            # son desechados
            if huevo[i][j] < 3:
                desechados.append("[" + str(i) + "][" + str(j) + "]")
                huevos_desechados += 1
            # son retirados
            if huevo[i][j] >= 8:
                retirados.append("[" + str(i) + "][" + str(j) + "]")
                huevos_retirados += 1

    print("\nResultados:")
    print("\n - Desechados: ")
    for desechado in desechados:
        print(desechado, end= ", ")
    print("\n - Retirados: ")
    for retirado in retirados:
        print(retirado, end= ", ")

    # Resumen
    print("\nResumen: " + str(huevos_desechados) + " huevos fueron desechados y " + str(huevos_retirados) + " huevos fueron retirados")