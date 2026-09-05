using System;
using System.Diagnostics.CodeAnalysis;
using static System.Runtime.InteropServices.JavaScript.JSType;
class Program
{
    static void Main()
    {
        Console.WriteLine("Введите длину массива: ");
        int n = int.Parse(Console.ReadLine());
        int[] a = new int[n];
        for (int i = 0; i < a.Length; ++i)
        {
            Console.Write("a[{0}]=", i);
            a[i] = int.Parse(Console.ReadLine());
        }
        Console.WriteLine("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}", Summ(a), Avg(a), PositiveSumm(a), NegativeSumm(a), oddIndexSumm(a), evenIndexSumm(a), IndexMax(a), IndexMin(a), Composition(a));
    }
    private static int Summ(int[] a) 
    {
        int res = 0;
        for (int i = 0; i < a.Length; ++i) res += a[i];
        return res;
    }
    private static double Avg(int[] a)
    {
        int summ = Summ(a);
        double avg = summ / a.Length;
        return avg;
    }
    private static int PositiveSumm(int[] a) 
    {
        int possumm = 0;
        for (int i = 0; i < a.Length; ++i) if (a[i] >= 0) possumm += a[i];
        return possumm;
    }
    private static int NegativeSumm(int[] a)
    {
        int negsumm = 0;
        for (int i = 0; i < a.Length; ++i) if (a[i] < 0) negsumm += a[i];
        return negsumm;
    }
    private static int oddIndexSumm(int[] a)
    {
        int oddindexsumm = 0;
        for (int i = 0; i < a.Length; ++i) if (i % 2 == 1) oddindexsumm += a[i];
        return oddindexsumm;
    }
    private static int evenIndexSumm(int[] a)
    {
        int evenindexsumm = 0;
        for (int i = 0; i < a.Length; ++i) if (i % 2 == 0) evenindexsumm += a[i];
        return evenindexsumm;
    }
    private static int IndexMax(int[] a)
    {
        int indexmax = 0;
        int max = -9999999;
        for (int i = 0;i < a.Length; ++i)
        {
            if (a[i] > max)
            {
                max = a[i];
                indexmax = i;
            }
        }
        return indexmax;
    }
    private static int IndexMin(int[] a)
    {
        int indexmin = 0;
        int min = 9999999;
        for (int i = 0; i < a.Length; ++i)
        {
            if (a[i] < min)
            {
                min = a[i];
                indexmin = i;
            }
        }
        return indexmin;
    }
    private static int Composition(int[] a)
    {
        int comp = 1;
        int mn = IndexMin(a);
        int mx = IndexMax(a);
        for (int i = mn + 1; i < mx; ++i) comp = comp * a[i];
        return comp;
    }
}