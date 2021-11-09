using System;

namespace matriz5x5
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] M;
            M = new int[5,5];

            int x,y;
            for(x = 0; x < 5 ; x++)
            {
                for(y = 0; y < 5; y++)
                {
                    // se consulta si es la diagonal principal
                    if(x == y)
                        M[x,y] = 0;
                    else
                        //se consulta si es la diagonal secundaria
                        if(x+y == 4)
                            M[x,y] = 0;
                        else
                            M[x,y] = 1;
                }
            }

            //imprimir la matriz
            
            for(x = 0; x < 5 ; x++)
            {
                for(y = 0; y < 5; y++)
                {
                    Console.Write(M[x,y] + " ");
                }
                Console.WriteLine(" ");
            }
        }
    }
}
