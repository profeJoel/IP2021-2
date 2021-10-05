using System;

namespace Clase8
{
    class Program
    {
        //Ejercicio 1
        //Si es de tipo void, entonces no tiene retorn
        static void Escribir(string texto){
            Console.WriteLine(texto);
        }

        //Ejercicio 2
        //si es de tipo Int, el return debe ser int
        static int Leer(){
            int datoEntrada;
            datoEntrada = Convert.ToInt32(Console.ReadLine());
            return datoEntrada;
        }

        //Ejercicio 3
        static double Sumatoria1(int n){
            int i;
            double valorParcial, sumatoria = 0;
            //i=i+1 => i+=1 => i++, son equivalentes
            for(i = 1; i <= n; i++){
                valorParcial = (double) (2*i+1)/(4*i); //se aplica un casting para obligar el cambio de tipo de datos para la operación
                Escribir("valor parcial [" + i + "] : " + valorParcial);
                //sumatoria = sumatoria + valorParcial; //son equivalentes
                sumatoria += valorParcial;
            }
            return sumatoria;
        }

        static void Main(string[] args)
        {
            Escribir("Hola, esta es la clase práctica 8!!!");
            Escribir("Ingrese un número: ");
            int numero = Leer();
            Escribir("El número ingresado es: " + numero);

            double resultado = Sumatoria1(numero);
            Escribir("EL resultado de la sumatoria es: " + resultado);
        }
    }
}
