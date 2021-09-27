using System;

namespace MayorEdad
{
    class Program
    {
        static void Main(string[] args)
        {
            int edad;
            Console.WriteLine("Ingrese Edad:");
            edad = Convert.ToInt32(Console.ReadLine());

            if(edad >= 0 && edad <= 130)
            {
                if(edad >= 18)
                {
                    Console.WriteLine("Es Mayor de Edad");
                }
                else
                {
                    Console.WriteLine("Es Menor de Edad");
                }
            }
            else
            {
                Console.WriteLine("Error: Valor edad no permitida");
            }
        }
    }
}
