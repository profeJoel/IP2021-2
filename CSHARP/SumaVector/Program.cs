using System;

namespace SumaVector
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, suma = 0;
            int[] numeros = new int[8];

            for(i=0; i<8; i++)
            {
                Console.WriteLine("Ingrese el " + (i+1) +"° valor: ");
                numeros[i] = Convert.ToInt32(Console.ReadLine());

                suma = suma + numeros[i];
            }

            Console.WriteLine("El total de la suma es: " + suma);
        }
    }
}
