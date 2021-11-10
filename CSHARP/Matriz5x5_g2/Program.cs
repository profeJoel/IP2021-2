using System;

namespace Matriz5x5_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] M;
            M = new int[5,5];

            int f,c;
            for(f=0; f<5; f++)
            {
                for(c=0; c<5; c++)
                {
                    //consultar si es la diagonal principal
                    if(f==c)
                        M[f,c] = 0;
                    else
                        //consultar si es la diagonal secundaria
                        if(f+c==4)
                            M[f,c] = 0;
                        else
                            M[f,c] = 1;
                }
            }

            Console.WriteLine("La matriz es: ");
            
            for(f=0; f<5; f++)
            {
                for(c=0; c<5; c++)
                {
                    Console.Write(M[f,c] + " ");
                }
                Console.WriteLine(" ");
            }
        }
    }
}
