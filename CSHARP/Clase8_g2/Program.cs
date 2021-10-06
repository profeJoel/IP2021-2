using System;

namespace Clase8_g2
{
    class Program
    {
        //Ejercicio 1
        // se utiliza el tipo de datos void para denotar que la función NO RETORNARÁ algún valor
        static void Escribir(string texto){
            Console.WriteLine(texto);
        }

        //Ejercicio 2
        static int Leer(){
            int datoEntrada;
            datoEntrada = Convert.ToInt32(Console.ReadLine());
            return datoEntrada;
        }

        //Ejercicio 3
        static double Sumatoria1(int n){
            int i;
            double valorParcial, sumatoria = 0;
            //i = i + 1; => i += 1; => i++; Son equivalentes
            for(i = 1; i <= n; i++){
                valorParcial = (double) (2*i+1)/(4*i);// casting es un cambio momentaneo de tipo de dato para la operación
                Escribir("Valor Parcial [" + i + "] : " + valorParcial);
                //sumatoria = sumatoria + valorParcial; //Equivalentes
                sumatoria += valorParcial;
            }
            return sumatoria;
        }

        static void Main(string[] args)
        {
            int numero;
            double resultado;
            Escribir("Hola, Esta es la clase práctica del grupo 2");// la llamada a la función puede realizarse muchas veces
            Escribir("Ingrese un valor entero:");
            numero = Leer();
            Escribir("El valor ingresado es: " + numero);

            resultado = Sumatoria1(numero);
            Escribir("El resultado de la sumatoria es: " + resultado);
        }
    }
}
