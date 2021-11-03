using System;

namespace Ejercicio1
{
    class Program
    {
        static double calcularIVA(double precioNeto)
        {
            double iva = precioNeto * 0.19;
            return iva;
        }
        static void Main(string[] args)
        {
            double totalNeto = 0, impuestoTotal = 0, montoBrutoTotal = 0, montoNeto, impuestoIVA;
            int opcion = 1;
            Console.WriteLine("Bienvenidos a Start-up Mariscos Ahumados");

            while(opcion == 1)
            {
                Console.WriteLine("Ingrese el valor neto del producto");
                montoNeto = Convert.ToDouble(Console.ReadLine());
                while(montoNeto <= 0)
                {
                    Console.WriteLine("Ingrese el valor neto del producto");
                    montoNeto = Convert.ToDouble(Console.ReadLine());
                }
                impuestoIVA = calcularIVA(montoNeto);
                
                totalNeto += montoNeto;
                impuestoTotal += impuestoIVA;
                montoBrutoTotal += montoNeto + impuestoIVA;

                //Console.WriteLine("Quiere ingresar otro precio de producto\n - Ingrese 1 para ingresar nuevo producto\n - Ingrese 0 para salir");
                Console.WriteLine("Quiere ingresar otro precio de producto");
                Console.WriteLine(" - Ingrese 1 para ingresar nuevo producto");
                Console.WriteLine(" - Ingrese 0 para salir");
                opcion = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine("\n\nResumen de la Compra:");
            Console.WriteLine(" - Total Neto: " + totalNeto);
            Console.WriteLine(" - Impuesto Total: " + impuestoTotal);
            Console.WriteLine(" - Monto Bruto Total: " + montoBrutoTotal);
        }
    }
}
