using System;

namespace Funcion1
{
    class Program
    {
        static void Main(string[] args)
        {
            double x, f;
            Console.WriteLine("Ingrese el valor de X");
            x = Convert.ToDouble(Console.ReadLine());

            f = ((x+1)*(x+1)) + ((2*x)*(2*x)); // (x+1)^2 + (2x)^2, la operación de potencia no es permitida en C#

            Console.WriteLine("El resultado es: " + f);
        }
    }
}
