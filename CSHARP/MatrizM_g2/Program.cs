using System;
using System.IO;

namespace MatrizM_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            char[,] M;
            M = new char[5,5];

            int f,c;

            for(f=0; f<5; f++)
            {
                for(c=0; c<5; c++)
                {
                    if(c==0 || c==4)
                    {
                        M[f,c] = 'm';
                    }
                    else
                    {
                        if(f==1 && (c==1 || c==3))
                        {
                            M[f,c] = 'm';
                        }
                        else
                        {
                            if(f==2 && c==2)
                            {
                                M[f,c] = 'm';
                            }
                            else
                            {
                                M[f,c] = ' ';
                            }
                        }
                    }
                }
            }

            /*Console.WriteLine("La Matriz M es:\n");
            
            for(f=0; f<5; f++)
            {
                for(c=0; c<5; c++)
                {
                    Console.Write(M[f,c] + " ");
                }
                Console.WriteLine(" ");
            }*/

            //Crear el archivo
            //Añadir texto al final del archivo
            using(StreamWriter archivo = File.CreateText("letraM.txt")) // Esta línea me permite crear y escribir sobre un archivo
            {
                for(f=0; f<5; f++)
                {
                    for(c=0; c<5; c++)
                    {
                        archivo.Write(M[f,c] + " ");
                    }
                    archivo.WriteLine(" ");
                }
            }
        }
    }
}
