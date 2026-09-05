using System;
class Program
{
    static void Main()
    {
        Book b2 = new Book("Толстой Л.Н.", "Война и мир", "Наука и жизнь", 1234, 2013, 101, true);
        b2.TakeItem();
        Magazine mag1 = new Magazine("О природе", 5, "Земля и мы", 2014, 1235, true);
        Console.WriteLine("\n Тестирование полиморфизма");
        Item it;
        it = b2;
        it.TakeItem();
        it.Return();
        it.Show();
        it = mag1;
        it.TakeItem();
        it.Return();
        it.Show();
    }
}