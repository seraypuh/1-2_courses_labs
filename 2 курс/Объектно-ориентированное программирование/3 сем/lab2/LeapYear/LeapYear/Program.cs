using System;
class Program
{
    static void Main()
    {
        int year = int.Parse(Console.ReadLine());
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
            Console.WriteLine("Високосный");
        else Console.WriteLine("Не високосный");
    }
}