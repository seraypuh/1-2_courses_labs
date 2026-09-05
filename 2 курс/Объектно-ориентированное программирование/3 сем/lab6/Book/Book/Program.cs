using System;
class Program
{
    static void Main()
    {
        Triangle abc = new Triangle(3, 4, 5);
        abc.Sides();
        Console.WriteLine(abc.Perimeter());
        Console.WriteLine(abc.Square());
        Console.WriteLine(abc.Exist());
    }
}