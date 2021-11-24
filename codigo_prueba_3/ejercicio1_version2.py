import random

if __name__ == "__main__":
    huevos_desechados = 0
    huevos_retirados = 0

    desechados_i = [None] * 30
    desechados_j = [None] * 30
    indice_desechados = 0

    retirados_i = [None] * 30
    retirados_j = [None] * 30
    indice_retirados = 0

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
                #print("Huevo en la posicion [" + str(i) + "]["+str(j)+"] es DESECHADO")
                desechados_i[indice_desechados] = i
                desechados_j[indice_desechados] = j
                indice_desechados += 1
                huevos_desechados += 1
            # son retirados
            if huevo[i][j] >= 8:
                #print("Huevo en la posicion [" + str(i) + "]["+str(j)+"] es RETIRADO")
                retirados_i[indice_retirados] = i
                retirados_j[indice_retirados] = j
                indice_retirados += 1
                huevos_retirados += 1

    print("\nResultados:")
    print("\n - Desechados: ")
    for i in range(indice_desechados):
        print("[" + str(desechados_i[i]) + "][" + str(desechados_j[i]) + "]", end= ", ")
    print("\n - Retirados: ")
    for i in range(indice_retirados):
        print("[" + str(retirados_i[i]) + "][" + str(retirados_j[i]) + "]", end= ", ")

    # Resumen
    print("\nResumen: " + str(huevos_desechados) + " huevos fueron desechados y " + str(huevos_retirados) + " huevos fueron retirados")