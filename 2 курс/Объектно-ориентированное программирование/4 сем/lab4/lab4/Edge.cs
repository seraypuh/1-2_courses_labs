using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Edge
{
    public int Source;
    public int Destination;
    public int Weight;

    public Edge(int s, int d, int w)
    {
        Source = s;
        Destination = d;
        Weight = w;
    }
}