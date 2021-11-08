using System;

namespace Strings
{
    class Program
    {
        static int contarLetras(String texto)
        {
            return texto.Length;
        }

        static void Main(string[] args)
        {
            String palabra1, palabra2;
            Console.WriteLine("Ingrese una palabra: ");
            palabra1 = Console.ReadLine();
            Console.WriteLine("Ingrese otra palabra: ");
            palabra2 = Console.ReadLine();

            //Console.WriteLine("La cantidad de letras de esta palabra son: " + contarLetras(palabra));

            if(contarLetras(palabra1) > contarLetras(palabra2))
                Console.WriteLine("Palabra: " + palabra1 + " es más larga con " + contarLetras(palabra1) + " caracteres");
            else
                if(contarLetras(palabra1) == contarLetras(palabra2))
                    Console.WriteLine("Las palabras: " + palabra1 + " y " + palabra2 + " tienen igual largo, con " + contarLetras(palabra1) + " caracteres");
                else
                    Console.WriteLine("Palabra: " + palabra2 + " es más larga con " + contarLetras(palabra2) + " caracteres");
        }
    }
}
