using System;

class TriangleArea
{
    static void Main()
    {
        try
        {
            string a;
            Console.WriteLine("Please enter the perimeter of the triange:");
            a = Console.ReadLine();
            double i = double.Parse(a);
            double side = i / 3;
            double p = i / 2;
            double area = Math.Sqrt(p * (p - side) * (p - side) * (p - side));
            double rSide, rArea;
            rSide = Math.Round(side, 2);
            rArea = Math.Round(area, 2);
            Console.WriteLine("Side  |  Area");
            Console.WriteLine("{0}  |  {1}", rSide, rArea);
        }
        catch(Exception e)
        { 
            Console.WriteLine("Exception: {0}", e.Message);
        }
    }
}