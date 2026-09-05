using System;
class Program
{
    static void Main()
    {
        IProgression ar = new ArithmeticProgression(2, 5);
        IProgression geom = new GeometricProgression(3, 2);
        Console.WriteLine(ar.GetElement(5));
        Console.WriteLine(geom.GetElement(4));
    }
}
