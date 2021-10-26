using System;

namespace FuncionAnguloTriangulo
{
    class Program
    {
        static double calcularAnguloTriangulo(double a, double b)
        {
            double angulo, c;
            if(a <= 0 || b <= 0)
            {
                Console.WriteLine("Error, los valores deben ser positivos!!!");
                return 0;
            }
            else
            {
                c = Math.Sqrt(a*a+b*b);
                angulo = Math.Asin(a/c);
                return angulo;
            }
        }


        static void Main(string[] args)
        {
            double a, b, angulo;
            Console.WriteLine("Ingrese el valor de a: ");
            a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Ingrese el valor de b: ");
            b = Convert.ToDouble(Console.ReadLine());

            angulo = calcularAnguloTriangulo(a,b);
            Console.WriteLine("El angulo buscado es: " + angulo);
        }
    }
}
