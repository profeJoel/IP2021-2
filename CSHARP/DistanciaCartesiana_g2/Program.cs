using System;

namespace DistanciaCartesiana_g2
{
    class Program
    {
        static void Main(string[] args)
        {
            double x1,y1, x2,y2, d;
            Console.WriteLine("Ingrese el primer punto cartesiano:");
            x1 = Convert.ToDouble(Console.ReadLine());
            y1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Punto Ingresado: (" + x1 + "," + y1 + ")");
            
            Console.WriteLine("Ingrese el segundo punto cartesiano:");
            x2 = Convert.ToDouble(Console.ReadLine());
            y2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Punto Ingresado: (" + x2 + "," + y2 + ")");

            d = Math.Sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)));

            Console.WriteLine("La distancia Cartesiana es: " + d);
        }
    }
}
