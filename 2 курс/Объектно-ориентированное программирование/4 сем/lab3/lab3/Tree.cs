using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
public class Tree
{
    public Tree Left;
    public Tree Right;
    public char Value;
    public bool flag;
    public static List<char> list = new List<char>();
    public static Tree Node;
    public Tree()
    {
        Node = null;
    }
    public Tree(Tree left, Tree right, char val)
    {
        Value = val;
        Left = left;
        Right = right;
    }

    public void Add(ref Tree node, char value)
    {
        if (node == null)
        {
            node = new Tree(null, null, value);
            flag = false;
        }
        else if (node.Value != '.' && flag == false)
        {
            if (node.Left != null)
            {
                Add(ref node.Left, value);
                if (flag == false)
                {
                    if (node.Right != null)
                    {
                        Add(ref node.Right, value);
                    }
                    else
                    {
                        node.Right = new Tree(null, null, value);
                        flag = true;
                    }
                }
            }
            else
            {
                node.Left = new Tree(null, null, value);
                flag = true;
            }
        }
    }

    public void PrintTree(Tree node)
    {
        if (node == null) return;
        if (node.Value != '.')
        {
            Console.WriteLine("значение " + node.Value + " левый " + node.Left.Value + " правый " + node.Right.Value);
        }

        PrintTree(node.Left);
        PrintTree(node.Right);
    }
    public static void TreeWalk_Pr(Tree node)
    {
        if (node.Value != '.')
        {
            list.Add(node.Value);
            TreeWalk_Pr(node.Left);
            TreeWalk_Pr(node.Right);
        }
    }
    public static List<char> TreeWalk_Obr(Tree node)
    {
        if (node.Value == '.') return new List<char>();
        var result = TreeWalk_Obr(node.Left);
        result.Add(node.Value);
        result.AddRange(TreeWalk_Obr(node.Right));
        return result;
    }
    public static void TreeWalk_K(Tree node)
    {
        if (node == null) return;
        if (node.Value != '.')
        {
            TreeWalk_K(node.Left);
            TreeWalk_K(node.Right);
            list.Add(node.Value);
        }
    }
    public static int CalcTree(Tree node)
    {
        if (node == null) return 0;
        if (char.IsDigit(node.Value)) return node.Value - '0';
        int num1, num2;
        num1 = CalcTree(node.Left);
        num2 = CalcTree(node.Right);
        switch (node.Value)
        {
            case '+': return num1 + num2;
            case '-': return num1 - num2;
            case '*': return num1 * num2;
            case '/': return num1 / num2;
            default: return 0;
        }
    }
}