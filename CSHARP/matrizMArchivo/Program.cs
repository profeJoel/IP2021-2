using System;
using System.IO;

namespace matrizMArchivo
{
    class Program
    {
        static void Main(string[] args)
        {
            char[,] M;
            M = new char[5,5];

            int i,j;

            //i es el indice de las filas y j es el indice de las columnas
            for(i=0; i<5; i++)
            {
                for(j=0; j<5; j++)
                {
                    //condiciones por las columnas
                    if(j==0 || j==4)
                        M[i,j] = 'm';
                    else
                        //condiciones para las diagonales parciales
                        if(i==j && i<3)
                            M[i,j] = 'm';
                        else
                            if(i+j == 4 && i<3)
                                M[i,j] = 'm';
                            else
                                M[i,j] = ' ';
                }
            }
            
            //Mostrar la matriz por pantalla
            /*
            for(i=0; i<5; i++)
            {
                for(j=0; j<5; j++)
                {
                    Console.Write(M[i,j] + " ");
                }
                Console.WriteLine(" ");
            }*/
 
            //Crear archivo y se añade el texto de la matriz
            using(StreamWriter archivo = File.CreateText("letraM.txt"))
            {
                for(i=0; i<5; i++)
                {
                    for(j=0; j<5; j++)
                    {
                        archivo.Write(M[i,j] + " ");
                    }
                    archivo.WriteLine(" ");
                }
            }
        }
    }
}
