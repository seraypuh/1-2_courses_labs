using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Generation
{
    public int a;
    public int b;
    public int c;
    public int d;
    public static Random r = new Random();
    public int ex_res;
    public Func<int, int, int, int, int> f;
    private int? real_res;

    public int RealResult
    {
        get
        {
            if (real_res == null)
            {
                real_res = f(a, b, c, d);
            }
            return (int)real_res;
        }
    }

    public Generation(Func<int, int, int, int, int> f, int a, int b, int c, int d, int ex_res)
    {
        this.f = f;
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.ex_res = ex_res;
    }
    public static Generation NewGen(Generation p1, Generation p2)
    {
        int x = r.Next(1, 4);
        switch (x)
        {
            case 1: return new Generation(p1.f, p1.a, p1.b, p2.c, p2.d, p2.ex_res);
            case 2: return new Generation(p1.f, p1.a, p2.b, p2.c, p2.d, p2.ex_res);
            case 3: return new Generation(p1.f, p1.a, p1.b, p1.c, p2.d, p2.ex_res);
            default: return null;
        }
    }
    public void Change()
    {
        int imposter = r.Next(1, 5);
        switch (imposter)
        {
            case 1:
                a = r.Next(1, 30);
                break;
            case 2:
                b = r.Next(1, 30);
                break;
            case 3:
                c = r.Next(1, 30);
                break;
            case 4:
                d = r.Next(1, 30);
                break;
            default:
                break;
        }
    }
    public int GetAc()
    {
        return Math.Abs((int)(ex_res - RealResult));
    }

    public static double SrKoef(List<Generation> generations)
    {
        double sum = 0;
        foreach (Generation item in generations)
        {
            sum += item.GetAc();
        }
        return sum / generations.Count();
    }
}