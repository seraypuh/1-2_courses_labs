using System;
using static System.Runtime.InteropServices.JavaScript.JSType;
class Program
{
    static void Main()
    {
        int[] MyArray;
        int n = int.Parse(Console.ReadLine());
        MyArray = new int[n];
        for (int i = 0; i < MyArray.Length; ++i)
        {
            Console.Write("a[{0}]=", i);
            MyArray[i] = int.Parse(Console.ReadLine());
        }
        foreach (int x in MyArray) Console.Write("{0} ", x);
        for (int i = 0; i < MyArray.Length; i++)
        {
            if (MyArray[i] % 2 == 0) MyArray[i] = 0;
            Console.Write("{0} ", MyArray[i]);
        }
    }
}
