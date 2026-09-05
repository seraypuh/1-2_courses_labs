using System;
class Program
{
    static void Main()
    {
        Progression ar = new ArithmeticProgression(2, 5);
        Progression geom = new GeometricProgression(3, 2);
        Console.WriteLine(ar.GetElement(5));
        Console.WriteLine(geom.GetElement(4));
    }
}
