using System;

namespace Funcion1_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            double x, f;
            Console.WriteLine("Ingrese un valor");
            x = Convert.ToDouble(Console.ReadLine());

            f = ((x+1)*(x+1)) + ((2*x)*(2*x)); //es equivalente a (x+1)^2 + (2*x)^2

            Console.WriteLine("El resultado es " + f);
        }
    }
}
