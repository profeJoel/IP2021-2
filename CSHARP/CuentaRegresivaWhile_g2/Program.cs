using System;

namespace CuentaRegresivaWhile_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 10;
            while(n >= 0)
            {
                Console.WriteLine(n);
                n = n - 1;
            }

            Console.WriteLine("Feliz Año Nuevo");
        }
    }
}
