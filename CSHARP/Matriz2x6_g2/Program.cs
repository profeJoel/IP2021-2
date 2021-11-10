using System;

namespace Matriz2x6_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] M;
            M = new int[2,6];

            int i,j, par = 0, impar = 0;
            for(i=0; i <2; i++)
            {
                for(j=0; j< 6; j++)
                {
                    Console.WriteLine("Ingrese el valor ["+i+","+j+"]: ");
                    M[i,j] = Convert.ToInt32(Console.ReadLine());

                    if(M[i,j] % 2 == 0)
                        par++;
                    else
                        impar++;
                }
            }

            Console.WriteLine("\nLa matriz es:");
            
            for(i=0; i <2; i++)
            {
                for(j=0; j< 6; j++)
                {
                    Console.Write(M[i,j] + " ");
                }
                Console.WriteLine(" ");
            }

            Console.WriteLine("\nLa cantidad de números Pares es: " + par);
            Console.WriteLine("La cantidad de números Impares es: " + impar);
        }
    }
}
