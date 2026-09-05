using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class ArithmeticProgression : Progression
{
    private double a1;
    private double d;
    public ArithmeticProgression(double a1, double d)
    {
        this.a1 = a1;
        this.d = d;
    }
    public override double GetElement(int k)
    {
        return a1 + (k - 1) * d;
    }
}
