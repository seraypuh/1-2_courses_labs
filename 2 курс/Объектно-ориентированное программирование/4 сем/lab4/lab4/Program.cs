using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Graph graph = new Graph(4);

        graph.AddEdge(0, 1, 10);
        graph.AddEdge(0, 2, 6);
        graph.AddEdge(0, 3, 5);
        graph.AddEdge(1, 3, 15);
        graph.AddEdge(2, 3, 4);

        graph.Kruskal();
    }
}