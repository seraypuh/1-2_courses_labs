using System;
class Program
{
    static void Main()
    {
        try
        {
            Random random = new Random();
            double x, y;
            int score = 0;
            Console.Write("Количество выстрелов: ");
            int shoots = int.Parse(Console.ReadLine());
            Console.Write("Стрельба вслепую? Введите 'ДА' если согласны, если нет, то любой иной ответ: ");
            string choice = Console.ReadLine();
            Console.WriteLine("|| Попадание в окружность радиусом 1 от центра мишени - 10 баллов, радиусом 2 - 5 баллов, иначе - 0 баллов ||");
            if (choice == "ДА")
            {
                int xcenter = random.Next(10);
                int ycenter = random.Next(10);
                for (int i = 0; i < shoots; i++)
                {
                    Console.WriteLine("Выстрел номер {0}:", i + 1);
                    Console.Write("X = ");
                    x = double.Parse(Console.ReadLine()) + random.NextDouble();
                    Console.Write("Y = ");
                    y = double.Parse(Console.ReadLine()) + random.NextDouble();
                    if ((x - xcenter) * (x - xcenter) + (y - ycenter) * (y - ycenter) <= 1) score += 10;
                    else if ((x - xcenter) * (x - xcenter) + (y - ycenter) * (y - ycenter) <= 4) score += 5;
                }
            }
            else
            {
                Console.WriteLine("Центр = (0, 0)");
                for (int i = 0; i < shoots; i++)
                {
                    Console.WriteLine("Выстрел номер {0}:", i + 1);
                    Console.Write("X = ");
                    x = double.Parse(Console.ReadLine()) + random.NextDouble();
                    Console.Write("Y = ");
                    y = double.Parse(Console.ReadLine()) + random.NextDouble();
                    if (x * x + y * y <= 1) score += 10;
                    else if (x * x + y * y <= 4) score += 5;
                }
            }
            Console.WriteLine("Итоговый счёт: {0}", score);
        }
        catch (Exception e) { Console.WriteLine("Ошибка ввода."); }
    }
}