using System;

namespace FuncionAreaRectanguloG2
{
    class Program
    {
        //static <tipo_dato> <nombre_funcion>(<parámetros>)
        static double areaRectangulo(double b, double a)
        {
            double area;
            // || significa o lógico
            // && significa y lógico
            if(b <= 0 || a <= 0)
            {
                Console.WriteLine("Error, Los valores deben ser positivos");
                area = 0;
            }
            else
            {
                area = b * a;
            }

            return area;
        }

        //Es la función principal
        static void Main(string[] args)
        {
            double b,a;
            Console.WriteLine("Ingrese el valor de la Base: ");
            b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Ingrese el valor de la Altura: ");
            a = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("El área del rectángulo es: " + areaRectangulo(b,a));
        }
    }
}
