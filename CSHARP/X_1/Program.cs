using System;

namespace X_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int x;
            float x_1;
            Console.WriteLine("Ingrese un número");
            x = Convert.ToInt32(Console.ReadLine()); //Convierte el valor de String a Int
            x_1 = (float) 1 / x;

            Console.Write("El resultado es: ");
            Console.WriteLine(x_1);
        }
    }
}
