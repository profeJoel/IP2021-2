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
    # range permite crear un conjunto de numero entre 1 y el n + 1
    # range(n) = [0,1,2,3,...,n-1]
    # range(5) = [0,1,2,3,4]
    #
    # range(a,b) = [a, a+1, a+2, ... , b-2, b-1]
    # range(3,8) = [3,4,5,6,7]
    # range(1,n+1) = [1,2,3,4,...,n]
    # range(1,3+1) = [1,2,3]
    for i in range(1,n+1):
        valor_parcial = (float) (2*i+1)/(4*i)
        escribir("Valor parcial [" + str(i) + "] : " + str(valor_parcial))
        #sumatoria = sumatoria + valor_parcial
        sumatoria += valor_parcial
    
    return sumatoria

if __name__ == "__main__":
    escribir("Hola, esta es la clase práctica 8")
    escribir("Ingrese un número: ")
    numero = leer()
    escribir("El número ingresado es: " + str(numero))

    resultado = sumatoria_1(numero)
    escribir("El resultado de la sumatoria es: " + str(resultado))