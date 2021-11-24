import random

if __name__ == "__main__":
    huevos_desechados = 0
    huevos_retirados = 0

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
                print("Huevo en la posicion [" + str(i) + "]["+str(j)+"] es DESECHADO")
                huevos_desechados += 1
            # son retirados
            if huevo[i][j] >= 8:
                print("Huevo en la posicion [" + str(i) + "]["+str(j)+"] es RETIRADO")
                huevos_retirados += 1

    # Resumen
    print("\nResumen: " + str(huevos_desechados) + " huevos fueron desechados y " + str(huevos_retirados) + " huevos fueron retirados")