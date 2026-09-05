using System;
class Program
{
    static void Main()
    {
        int a, b, c;
        Console.WriteLine("Введите коэффициент a: ");
        a = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите коэффициент b: ");
        b = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите коэффициент c: ");
        c = int.Parse(Console.ReadLine());
        double x1, x2;
        if (Operation.Equation(a, b, c, out x1, out x2))
        {
            if (x1 == x2) Console.WriteLine("Корень уравнения с коэффициентами a = {0}, b = {1}, c = {2} равен x1 = x2 = {3}.", a, b, c, x1);
            else Console.WriteLine("Корни уравнения с коэффициентами a = {0}, b = {1}, c = {2} равны x1 = {3}, x2 = {4}.", a, b, c, x1, x2);
        }
        else Console.WriteLine("Корней уравнения с коэффициентами a = {0}, b = {1}, c = {2} нет.", a, b, c);
    }
}