using System;

public struct Distance
{
    public int foot;
    public int inch;
}
class Program
{
    static void Main()
    {
        try
        {
            // Определяем переменные
            Distance dist1;
            Distance dist2;
            Distance dist3;
            // Задаём значения первым двум
            Console.Write("Введите первое значение в футах: ");
            dist1.foot = int.Parse(Console.ReadLine());
            Console.Write("Введите первое значение в дюймах: ");
            dist1.inch = int.Parse(Console.ReadLine());
            Console.Write("Введите второе значение в футах: ");
            dist2.foot = int.Parse(Console.ReadLine());
            Console.Write("Введите второе значение в дюймах: ");
            dist2.inch = int.Parse(Console.ReadLine());
            // Задаём значение суммы двух переменных
            dist3.foot = dist1.foot + dist2.foot + ((dist1.inch + dist2.inch) / 12);
            dist3.inch = (dist1.inch + dist2.inch) % 12;
            Console.WriteLine("Сумма двух расстояний: {0}'-{1}''", dist3.foot, dist3.inch);
        }
        catch (Exception e)
        {
            Console.WriteLine("Ошибка! Некорректные данные!");
        }
    }
}