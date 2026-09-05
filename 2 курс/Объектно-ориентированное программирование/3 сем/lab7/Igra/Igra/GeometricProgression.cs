using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
class GeometricProgression : Progression
{
    private double b1;
    private double q;
    public GeometricProgression(double b1, double q)
    {
        this.b1 = b1;
        this.q = q;
    }
    public override double GetElement(int k)
    {
        return b1 * Math.Pow(q, k - 1);
    }
}

