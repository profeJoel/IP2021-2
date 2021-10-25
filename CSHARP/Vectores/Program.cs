using System;

namespace Vectores
{
    class Program
    {
        static void Main(string[] args)
        {
            int i;
            int[] datos = new int[3]; // Para resguardar las 3 posiciones se utiliza el comando new

            for(i=0; i<3; i++)
            {
                Console.WriteLine("Ingrese el " + (i+1) + "° valor: "); 
                datos[i] = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine("\nLos valores ingresados son:");
            for(i=0; i<3; i++)
                Console.WriteLine("datos["+i+"] = " + datos[i]);
        }
    }
}
