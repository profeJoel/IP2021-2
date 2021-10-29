using System;

namespace FuncionNumeroPositivo
{
    class Program
    {
        static bool esPositivo(int numero)
        {
            bool respuesta;
            respuesta = numero > 0; // almacenando el resultado de una consulta lógica (verdadero o falso)
            return respuesta;
        }

        static void Main(string[] args)
        {
            int numero;
            Console.WriteLine("Ingrese un número: ");
            numero = Convert.ToInt32(Console.ReadLine());

            //Console.WriteLine("EL resultado es: " + esPositivo(numero));

            if(esPositivo(numero))
                Console.WriteLine("El número es positivo");
            else
                Console.WriteLine("El Número es Negativo");
        }
    }
}
