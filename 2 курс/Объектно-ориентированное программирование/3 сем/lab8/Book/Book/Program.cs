using System;
class Program
{
    static void Main()
    {
        Book b1 = new Book();
        b1.SetBook("Пушкин А.С.", "Капитанская дочка", "Вильямс", 123, 2012);
        Book.SetPrice(12);
        Book b2 = new Book("Толстой Л.Н.", "Война и мир", "Наука и жизнь", 1234, 2013, 101, true);
        b2.TakeItem();
        Book b3 = new Book("Лермонтов М.Ю.", "Мцыри");
        Magazine mag1 = new Magazine("О природе", 5, "Земля и мы", 2014, 1235, true);
        Item[] itmas = new Item[4];
        itmas[0] = b1;
        itmas[1] = b2;
        itmas[2] = b3;
        itmas[3] = mag1;
        Array.Sort(itmas);
        Console.WriteLine("\nСортировка по инвентарному номеру");
        foreach (Item x in itmas)
        {
            x.Show();
        }



        /*Item it;
        it = b2;
        mag1.TakeItem();
        mag1.Show();
        mag1.IfSubs = true;
        mag1.Subs();
        it.TakeItem();
        it.Return();
        it.Show();
        it = mag1;
        it.TakeItem();
        it.Return();
        it.Show();*/
    }
}