using System;
using System.IO;

namespace listaAlumnos
{
    class Program
    {
        static void Main(string[] args)
        {
            int opcion, id = 1, edad;
            String nombre;
            Console.WriteLine("Bienvenido al programa de registro de estudiantes");
            opcion = 1;

            using(StreamWriter archivo = File.CreateText("lista_alumnos.csv"))
            {
                archivo.WriteLine("N, NOMBRE, EDAD");
            }

            //ciclo infinito
            while(opcion == 1)
            {
                Console.WriteLine("Ingrese el nombre del estudiante: ");
                nombre = Console.ReadLine();
                Console.WriteLine("Ingrese la edad del estudiante: ");
                edad = Convert.ToInt32(Console.ReadLine());
                while(edad <= 0 || edad >= 130)
                {
                    Console.WriteLine("Ingrese la edad del estudiante: ");
                    edad = Convert.ToInt32(Console.ReadLine());
                }

                using(StreamWriter archivo = File.AppendText("lista_alumnos.csv"))
                {
                    archivo.WriteLine(id + ", " + nombre + ", " + edad);
                }

                id++;

                Console.WriteLine("Desea ingresar otro estudiante? marque (1) para seguir o (0) para salir");
                opcion = Convert.ToInt32(Console.ReadLine());
                while(opcion<0 || opcion>1)
                {
                    Console.WriteLine("Desea ingresar otro estudiante? marque (1) para seguir o (0) para salir");
                    opcion = Convert.ToInt32(Console.ReadLine());
                }
            }
        }
    }
}
