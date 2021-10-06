
#Ejercicio 1
def escribir(texto):
    print(texto)

#Ejercicio 2
def leer():
    dato_entrada = int(input())
    return dato_entrada

#Ejercicio 3
def sumatoria_1(n):
    sumatoria = 0
    #range(n) -> [0, ..., n-1]
    #range(3) -> [0,1,2]

    #range(a,b) -> [a, a+1, a+2,..., b-2, b-1]
    #range(1,3) -> [1,2]
    #range(1,n+1) -> [1,2,..., n]
    #range(1,3+1) -> [1,2,3]

    for i in range(1, n+1):
        valor_parcial = (2*i+1)/(4*i)
        escribir("Valor Parcial [" + str(i) + "] : " + str(valor_parcial))
        #sumatoria = sumatoria + valor_parcial #equivalencia
        sumatoria += valor_parcial
    
    return sumatoria


#representación del main
if __name__ == "__main__":
    escribir("Hola, Esta es la clase práctica del grupo 2")

    escribir("Ingrese un valor entero:")
    numero = leer()
    escribir("El valor ingresado es: " + str(numero))

    resultado = sumatoria_1(numero)
    escribir("El resultado de la sumatoria es " + str(resultado))