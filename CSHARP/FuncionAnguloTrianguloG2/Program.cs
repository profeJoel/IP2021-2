using System;

namespace FuncionAnguloTrianguloG2
{
    class Program
    {
        static double angulo(double a, double b)
        {
            double bac, c;
            if(a <= 0 || b <= 0)
            {
                Console.WriteLine("Error, Los valores deben ser positivos");
                bac = 0;
            }
            else
            {
                c = Math.Sqrt(a*a + b*b);
                bac = Math.Asin(a/c);
            }

            return bac;
        }

        static void Main(string[] args)
        {
            double catetoA, catetoB, BAC;
            Console.WriteLine("Ingrese el valor del cateto a: ");
            catetoA = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Ingrese el valor del cateto b: ");
            catetoB = Convert.ToDouble(Console.ReadLine());

            BAC = angulo(catetoA, catetoB);
            Console.WriteLine("El valor del angulo del triangulo es: " + BAC);

        }
    }
}
