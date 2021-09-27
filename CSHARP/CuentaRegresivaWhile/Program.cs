using System;

namespace CuentaRegresivaWhile
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 10;
            while(n >= 0)
            {
                Console.WriteLine(n);
                n = n-1;
            }
        }
    }
}