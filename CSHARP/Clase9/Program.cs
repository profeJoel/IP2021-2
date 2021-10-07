using System;

namespace Clase9
{
    class Program
    {
        /*
        Concatenación
        texto1 = "Hola "
        texto2 = "Mundo"
        texto3 = texto1 + texto2 = "Hola " + "Mundo" = "Hola Mundo"
        */

        //Ejercicio 1
        static int Mayor(int a, int b){
            if(a > b){
                Console.WriteLine(a + " es mayor!!!");
                return a;
            }
            else{
                if(a < b){
                    Console.WriteLine(b + " es mayor!!!");
                    return b;
                }
                else{
                    Console.WriteLine(a + " y " + b + " son iguales");
                    return a;
                }
            }
        }

        //Ejercicio 2
        static int Menor(int a, int b){
            if(a < b){
                Console.WriteLine(a + " es menor!!!");
                return a;
            }
            else{
                if(a > b){
                    Console.WriteLine(b + " es menor!!!");
                    return b;
                }
                else{
                    Console.WriteLine(a + " y " + b + " son iguales");
                    return a;
                }
            }
        }

        //Ejercicio 3
        static double Potencia(int a, int b){
            int i;
            double p = 1; //neutro de la multiplicación
            bool esNeg = false; //booleano: {false, true}

            if(b < 0){
                b = -b;//obtengo el valor en positivo
                esNeg = true;
            }

            for(i=0; i<b; i++){
                //p = p*a; equivalente
                p *= (double) a;
            }

            if(esNeg){
                p = (double) 1/p;
            }

            return p;
        }

        static void Main(string[] args)
        {
            //Con una variable se almacena el retorno de la función
            int valorMayor = Mayor(4, 4);
            Console.WriteLine("El valor mayor es: " + valorMayor);

            //Se muestra el valor, pero no se almacena
            Console.WriteLine("El mayor valor es: " + Mayor(3,5));

            
            //Con una variable se almacena el retorno de la función
            int valorMenor = Menor(8, 4);
            Console.WriteLine("El valor menor es: " + valorMenor);

            //Se muestra el valor, pero no se almacena
            Console.WriteLine("El menor valor es: " + Menor(3,5));

            //double valorPotencia = Potencia(2, 9);
            double valorPotencia = Potencia(2, -2);
            Console.WriteLine("El valor de la potencia es: " + valorPotencia);
        }
    }
}
