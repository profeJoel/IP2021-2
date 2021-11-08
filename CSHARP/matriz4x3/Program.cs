using System;

namespace matriz4x3
{
    class Program
    {
        static void Main(string[] args)
        {
            int fila, filas = 4;
            int columna, columnas = 3;
            int suma = 0;

            int[,] M;
            M = new int[filas,columnas];

            for(fila = 0; fila < filas; fila++)
            {
                for(columna = 0; columna < columnas; columna++)
                {
                    //Estoy recorriendo cada posición de la matriz
                    Console.WriteLine("Ingrese un valor [" + fila +","+columna+"]: ");
                    M[fila,columna] = Convert.ToInt32(Console.ReadLine());
                }
            }

            Console.WriteLine("La matriz M es:");
            for(fila = 0; fila < filas; fila++)
            {
                for(columna = 0; columna < columnas; columna++)
                {
                    //Estoy recorriendo cada posición de la matriz
                    Console.Write(M[fila,columna] + " ");
                }
                Console.WriteLine(" ");//dar el salto de línea
            }

            //Suma de la matriz
            for(fila = 0; fila < filas; fila++)
            {
                for(columna = 0; columna < columnas; columna++)
                {
                    suma += M[fila,columna];
                }
            }

            Console.WriteLine("La suma es: " + suma);
        }
    }
}
