using System;
using System.Collections.Generic;
class Program
{
    static void Main(string[] args)
    {
        Tree t = new Tree();
        List<char> chars = new List<char>() { '/', '*', '+', '2', '.', '.', '3', '.', '.', '-', '7', '.', '.', '4', '.', '.', '3' };

        for (int i = 0; i < chars.Count; i++)
        {
            t.flag = false;
            t.Add(ref Tree.Node, chars[i]);
        }

        Console.WriteLine("Концевой порядок");
        Tree.TreeWalk_K(Tree.Node);
        foreach (var item in Tree.list)
        {
            Console.Write(item + " ");
        }

        Console.WriteLine("Выражение равно ");
        Console.Write(Tree.CalcTree(Tree.Node));
    }
}