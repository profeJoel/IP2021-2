using System;
using System.IO;

namespace listadoEstudiantes
{
    class Program
    {
        static void Main(string[] args)
        {
            int opcion = 1, n = 1, edad;
            String nombre;
            Console.WriteLine("Bienvenido al registro de estudiantes!");

            //Crear el archivo
            using(StreamWriter archivo = File.CreateText("listado.csv"))
            {
                archivo.WriteLine("N, NOMBRE, EDAD");
            }

            while(opcion == 1)
            {
                //pedir los datos
                Console.WriteLine("Ingrese el nombre del estudiante: ");
                nombre = Console.ReadLine();
                Console.WriteLine("Ingrese la edad del estudiante: ");
                edad = Convert.ToInt32(Console.ReadLine());
                while(edad < 0 || edad > 121)
                {
                    Console.WriteLine("Ingrese la edad del estudiante: ");
                    edad = Convert.ToInt32(Console.ReadLine());
                }

                // almacenarlos en un archivo
                using(StreamWriter archivo = File.AppendText("listado.csv"))
                {
                    archivo.WriteLine(n + ", " + nombre + ", " + edad);
                }
                n++;

                //continuar ingresando estudiantes
                Console.WriteLine("Desea ingresar un nuevo Usuario?\nMarque (1) para seguir o (0) para salir...");
                opcion = Convert.ToInt32(Console.ReadLine());
                while(opcion < 0 || opcion > 1)
                {
                    Console.WriteLine("Desea ingresar un nuevo Usuario?\nMarque (1) para seguir o (0) para salir...");
                    opcion = Convert.ToInt32(Console.ReadLine());
                }
            }
        }
    }
}
