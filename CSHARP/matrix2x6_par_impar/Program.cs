using System;

namespace matriz2x6_par_impar
{
    class Program
    {
        static void Main(string[] args)
        {
            int x,y, par = 0, impar = 0, filas = 2, columnas = 6;
            int[,] M;
            M = new int[filas,columnas];

            for(x = 0; x < filas; x++)
            {
                for(y = 0; y < columnas; y++)
                {
                    //Llenado de la matriz
                    Console.WriteLine("Ingrese el valor [" + x + "," + y + "]: ");
                    M[x,y] = Convert.ToInt32(Console.ReadLine());
                    
                    // si es par o impar
                    if(M[x,y]%2 == 0)
                        par++;
                    else
                        impar++;
                }
            }

            //imprimir matriz
            for(x = 0; x < filas; x++)
            {
                for(y = 0; y < columnas; y++)
                {
                    Console.Write(M[x,y] + " ");
                }
                Console.WriteLine(" ");
            }

            //Mostrar los resultados de par e impar
            Console.WriteLine("\nLa cantidad de Números Pares es: " + par);
            Console.WriteLine("La cantidad de Números Impares es: " + impar);
        }
    }
}
