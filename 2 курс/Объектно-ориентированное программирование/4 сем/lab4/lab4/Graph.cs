using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Graph
{
    private int vertices;
    private List<Edge> edges = new List<Edge>();

    public Graph(int v)
    {
        vertices = v;
    }

    public void AddEdge(int s, int d, int w)
    {
        edges.Add(new Edge(s, d, w));
    }

    public void Kruskal()
    {
        // Сортировка рёбер по весу
        edges.Sort((a, b) => a.Weight.CompareTo(b.Weight));

        int[] parent = new int[vertices];
        int[] rank = new int[vertices];

        // Инициализация Union-Find
        for (int i = 0; i < vertices; i++)
            parent[i] = i;

        List<Edge> result = new List<Edge>();

        foreach (var edge in edges)
        {
            int root1 = Find(parent, edge.Source);
            int root2 = Find(parent, edge.Destination);

            // Если не образуется цикл
            if (root1 != root2)
            {
                result.Add(edge);
                Union(parent, rank, root1, root2);
            }
        }

        Console.WriteLine("Минимальное остовное дерево:");
        int totalWeight = 0;

        foreach (var edge in result)
        {
            Console.WriteLine($"{edge.Source} - {edge.Destination} : {edge.Weight}");
            totalWeight += edge.Weight;
        }

        Console.WriteLine($"Общий вес: {totalWeight}");
    }

    private int Find(int[] parent, int i)
    {
        if (parent[i] != i)
            parent[i] = Find(parent, parent[i]); // Сжатие пути
        return parent[i];
    }

    private void Union(int[] parent, int[] rank, int x, int y)
    {
        if (rank[x] < rank[y])
            parent[x] = y;
        else if (rank[x] > rank[y])
            parent[y] = x;
        else
        {
            parent[y] = x;
            rank[x]++;
        }
    }
}
