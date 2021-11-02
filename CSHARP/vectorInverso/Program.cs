using System;

namespace vectorInverso
{
    class Program
    {
        static void Main(string[] args)
        {
            int n,i;
            Console.WriteLine("Ingrese el tamaño del vector");
            n = Convert.ToInt32(Console.ReadLine());
            while(n<=0)
            {
                Console.WriteLine("Ingrese el tamaño del vector");
                n = Convert.ToInt32(Console.ReadLine());
            }

            int[] v = new int[n]; //creación del vector con n posiciones

            for(i=0; i<n;i++)
            {
                Console.WriteLine("Ingrese un valor: ");
                v[i] = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine("Muestra Vector Inverso");
            for(i=n-1; i>=0; i--)
            {
                Console.WriteLine(v[i]);
            }
        }
    }
}
