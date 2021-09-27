using System;

namespace PerimetroAreaCirculo
{
    class Program
    {
        static void Main(string[] args)
        {
            double x, perimetro, area, pi;
            Console.WriteLine("Ingrese el diametro");
            x = Convert.ToDouble(Console.ReadLine());
            while(x<=0)
            {
                Console.WriteLine("Ingrese el diametro");
                x = Convert.ToDouble(Console.ReadLine());
            }
            // para mover el cursor a la derecha -> TAB
            // para mover el cursor a la izquierda <- Shift+TAB

            pi = 3.14; //utilizar el punto flotante inglés

            perimetro = pi * x; // equivalente a 2*pi*radio
            area = (pi*x*x)/4; // equivalente a pi*radio^2

            Console.WriteLine(perimetro);
            Console.WriteLine(area);
        }
    }
}
