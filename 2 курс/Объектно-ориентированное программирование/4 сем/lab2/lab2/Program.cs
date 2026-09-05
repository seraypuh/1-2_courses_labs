using System;
class Program
{
    public static int res = 30;
    public static Func<int, int, int, int, int> f = (a, b, c, d) => a + 2 * b + 3 * c + 4 * d;
    public static Random r = new Random();

    static void Main(string[] args)
    {
        List<Generation> generations = new List<Generation>();
        for (int i = 0; i < 5; i++)
        {
            generations.Add(new Generation(f, r.Next(1, 30), r.Next(1, 30), r.Next(1, 30), r.Next(10, 30), res));
        }

        for (int i = 0; i < 1000; i++)
        {
            Console.WriteLine("Итерация " + (i + 1));
            foreach (var item in generations)
            {
                Console.Write("a = " + item.a + " b = " + item.b + " c = " + item.c + " d = " + item.d + "\n");
            }
            Console.WriteLine("---");
            double koef1 = Generation.SrKoef(generations);
            var best = generations
                .OrderBy(g => g.GetAc())
                .ToList();

            if (best.Any(g => g.RealResult == res))
            {
                Solution(best[0]);
                break;
            }

            generations.Clear();
            generations.Add(Generation.NewGen(best[0], best[1]));
            generations.Add(Generation.NewGen(best[1], best[0]));
            generations.Add(Generation.NewGen(best[0], best[2]));
            generations.Add(Generation.NewGen(best[2], best[0]));
            generations.Add(Generation.NewGen(best[1], best[2]));

            double koef2 = Generation.SrKoef(generations);
            if (koef2 <= koef1)
            {
                Random ran = new Random();
                int x = ran.Next(1, 5);
                for (int j = 0; j < x; j++)
                {
                    generations[ran.Next(0, 5)].Change();
                }
            }
        }
    }
    public static void Solution(Generation g)
    {
        Console.WriteLine("Решение: ");
        Console.Write("a = " + g.a + " b = " + g.b + " c = " + g.c + " d = " + g.d + "\n");
    }
}