using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Operation
{
    public static double Geron(int a, int b, int c)
    {
        bool ok = Operation.Triangle(a, b, c);
        if (ok)
        {
            double p = (a + b + c) / 2;
            double s = Math.Sqrt(p * (p - a) * (p - b) * (p - c));
            return s;
        }
        else return 0;
    }
    private static bool Triangle(int a, int b, int c)
    {
        bool res = false;
        if ((a + b > c) && (a + c > b) && (b + c > a))
        {
            res = true;
        }
        return res;
    }
    public static double Geron(int a)
    {
        double p = (a + a + a) / 2;
        double s = Math.Sqrt(p * (p - a) * (p - a) * (p - a));
        return s;
    }
    public static bool Equation(int a, int b, int c, out double x1, out double x2)
    {
        x1 = 0;
        x2 = 0;
        double D = b * b - 4 * a * c;
        if (D < 0)
        {
            return false;
        }
        else
        {
            x1 = (-b + Math.Sqrt(D)) / (2 * a);
            x2 = (-b - Math.Sqrt(D)) / (2 * a);
            return true;
        }
    }
}