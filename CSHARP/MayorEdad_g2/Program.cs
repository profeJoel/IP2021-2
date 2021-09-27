using System;

namespace MayorEdad_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            int edad;
            Console.WriteLine("Ingrese su edad: ");
            edad = Convert.ToInt32(Console.ReadLine());

            if(edad >= 0 && edad <= 130) //&& es equivalente al "y lógico"
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
                Console.WriteLine("Error: Valor edad no permitido");
            }

        }
    }
}
