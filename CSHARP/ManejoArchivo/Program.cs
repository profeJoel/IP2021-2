using System;
using System.IO;

namespace ManejoArchivo
{
    class Program
    {
        static void Main(string[] args)
        {
            //Creación de un Archivo
            /*
            Console.WriteLine("Vamos a Crear un Archivo");
            File.Create("nuevoArchivo.txt");
            Console.WriteLine("Archivo Creado");
            */

            //Leer archivo
            /*
            Console.WriteLine("Vamos a Leer un Archivo");
            String texto = File.ReadAllText("nuevoArchivo.txt");
            Console.WriteLine("El texto en el archivo es: \n" + texto);
            */

            //Añadir texto al final
            
            /*Console.WriteLine("Vamos a Escribir texto al final del archivo");
            String nuevoTexto = "\nEste es una nueva linea añadida al final";
            using(StreamWriter archivo = File.AppendText("nuevoArchivo.txt"))
            {
                archivo.WriteLine(nuevoTexto);
            }
            Console.WriteLine("Archivo actualizado");
            */

            //Sobrescribir un archivo
            /*
            Console.WriteLine("Vamos a Sobrescribir un archivo");
            String nuevoTexto = "\nEste es una nueva linea que sobrescribe la anterior";
            File.WriteAllText("nuevoArchivo.txt", nuevoTexto);
            Console.WriteLine("Archivo Sobrescrito");
            */

            //Eliminar Archivo
            
            /*
            Console.WriteLine("Vamos a Eliminar un archivo");
            File.Delete("nuevoArchivo.txt");
            Console.WriteLine("Archivo eliminado!!!");
            */
        }
    }
}
