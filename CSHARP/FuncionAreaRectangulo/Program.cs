using System;

namespace FuncionAreaRectangulo
{
    class Program
    {
        static double calcularAreaRectangulo(double b, double altura)
        {
            double area;
            if(b <= 0 || altura <= 0)
            {
                Console.WriteLine("Error, los valores deben ser positivos!!!");
                return 0;
            }
            else
            {
                area = b * altura;
                return area;
            }
        }

        static void Main(string[] args)
        {
            double b, altura;
            //ingresar los valores desde la consola
            Console.WriteLine("Ingrese el valor de la base: ");
            b = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Ingrese el valor de la altura: ");
            altura = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("El área del rectangulo es " + calcularAreaRectangulo(b, altura));

        }
    }
}
