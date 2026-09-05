using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Triangle
{
    private int a;
    private int b;
    private int c;
    public Triangle(int a, int b, int c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public void Sides()
    {
        Console.WriteLine("{0} {1} {2}", a, b, c);
    }
    public int Perimeter()
    {
        return a + b + c;
    }
    public double Square()
    {
        double p = Perimeter() / 2;
        return Math.Sqrt(p * (p - a) * (p - b) * (p - c));
    }
    public bool Exist()
    {
        bool ex = false;
        if ((a < b + c) && (b < a + c) && (c < a + b))
        {
            ex = true;
        }
        return ex;
    }
}