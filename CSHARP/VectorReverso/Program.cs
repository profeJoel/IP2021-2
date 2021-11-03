using System;

namespace VectorReverso
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;

            Console.WriteLine("Ingrese la cantidad del elementos del vector");
            n = Convert.ToInt32(Console.ReadLine());
            while(n<=0)
            {
                Console.WriteLine("Ingrese la cantidad del elementos del vector");
                n = Convert.ToInt32(Console.ReadLine());
            }

            int[] v = new int[n]; //Creando un vector con n posiciones
            int i;
            
            for(i=0; i<n; i++) //i = [0,...,n-1]
            {
                Console.WriteLine("Ingrese los valores");
                v[i] = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine("Mostrar el vector al reverso");
            for(i=n-1; i >= 0; i--) //i = [n-1, ..., 0]
            {
                Console.WriteLine(v[i]);
            }
        }
    }
}
