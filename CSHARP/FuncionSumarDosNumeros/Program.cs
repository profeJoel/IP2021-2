using System;

namespace FuncionSumarDosNumeros
{
    class Program 
    {
        static int a; //es una variable global

        static int SumarDosNumeros(int numero1, int numero2){
            /*int resultado;
            resultado = numero1 + numero2;
            return resultado;*/
            a = a + 1;
            Console.WriteLine("El valor de a es " + a);
            return numero1 + numero2;
        }

        static void Main(string[] args)
        {
            /*
            int resultadoFuncion = SumarDosNumeros(1,2);
            Console.WriteLine("El resultado de la Funcion es " + resultadoFuncion);
            */
            a = 20;
            Console.WriteLine("El valor de a es " + a);

            Console.WriteLine("El resultado de la Funcion es " + SumarDosNumeros(1,2));

        }
    }
}
