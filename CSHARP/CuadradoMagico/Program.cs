using System;

namespace CuadradoMagico
{
    class Program
    {
        static bool EstaRepetido(int valor, int[] historial)
        {
            return historial[valor] == 1;
        }

        static void Main(string[] args)
        {
            int[] historial;
            historial = new int[10];

            int[,] M;
            M = new int[3,3];

            int i,j;
            int sumaFila0, sumaFila1, sumaFila2, sumaCol0, sumaCol1, sumaCol2, sumaDiag1, sumaDiag2;

            //0 - disponible
            //1 - ocupado
            historial[0] = 1;
            for(i=1; i<10; i++)
                historial[i] = 0;

            for(i=0; i<3; i++)
            {
                for(j=0; j<3; j++)
                {
                    Console.WriteLine("Ingrese el valor a la matriz ["+i+","+j+"]");
                    M[i,j] = Convert.ToInt32(Console.ReadLine());
                    while(M[i,j] < 1 || M[i,j] > 9)
                    {
                        Console.WriteLine("Valor incorrecto, Ingrese el valor a la matriz ["+i+","+j+"]");
                        M[i,j] = Convert.ToInt32(Console.ReadLine());
                    }
                    while(EstaRepetido(M[i,j], historial))
                    {
                        Console.WriteLine("Valor Repetido, Ingrese el valor a la matriz ["+i+","+j+"]");
                        M[i,j] = Convert.ToInt32(Console.ReadLine());
                        while(M[i,j] < 1 || M[i,j] > 9)
                        {
                            Console.WriteLine("Valor incorrecto, Ingrese el valor a la matriz ["+i+","+j+"]");
                            M[i,j] = Convert.ToInt32(Console.ReadLine());
                        }
                    }
                    historial[M[i,j]] = 1;
                }
            }

            Console.WriteLine("La matríz es:");
            for(i=0; i<3; i++)
            {
                for(j=0; j<3; j++)
                {
                    Console.Write(M[i,j] + " ");
                }
                Console.WriteLine(" ");
            }

            //Verificar si es un Cuadrado Mágico
            sumaFila0 = M[0,0] + M[0,1] + M[0,2];
            sumaFila1 = M[1,0] + M[1,1] + M[1,2];
            sumaFila2 = M[2,0] + M[2,1] + M[2,2];
            sumaCol0 = M[0,0] + M[1,0] + M[2,0];
            sumaCol1 = M[0,1] + M[1,1] + M[2,1];
            sumaCol2 = M[0,2] + M[1,2] + M[2,2];
            sumaDiag1 = M[0,0] + M[1,1] + M[2,2];
            sumaDiag2 = M[0,2] + M[1,1] + M[2,0];

            if(sumaFila0 == sumaFila1 && sumaFila1 == sumaFila2 && sumaCol0 == sumaCol1 && sumaCol1 == sumaCol2 && sumaFila0 == sumaCol0 && sumaCol0 == sumaDiag1 && sumaDiag1 == sumaDiag2)
                Console.WriteLine("Es un Cuadrado Mágico");
            else
                Console.WriteLine("NO es un Cuadrado Mágico");
        }
    }
}
