using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Book
{
    private String author; // а
    private String title; //  а!а "#
    private String publisher; // "!$а#%&'
    private int pages; // (%- 'а ")
    private int year;
    private static double price = 9;
    static Book()
    {
        price = 10;
    }
    public Book(String author, String title, String publisher, int pages, int year)
    {
        this.author = author;
        this.title = title;
        this.publisher = publisher;
        this.pages = pages;
        this.year = year;
    }
    public Book()
    { }
    public Book(String author, String title)
    {
        this.author = author;
        this.title = title;
    }
    public void SetBook(String author, String title, String publisher, int pages, int year)
    {
        this.author = author;
        this.title = title;
        this.publisher = publisher;
            this.pages = pages;
            this.year = year;
    }
    public static void SetPrice(double price)
    {
        Book.price = price;
    }
    public void Show()
    {
        Console.WriteLine("\nКнига: \n Автор: {0} \n Название: {1} \n Год издания: {2} \n {3} стр. \n Стоимость аренды: {4}", author, title, year, pages, Book.price);
    }
    public double PriceBook(int s)
    {
        double cust = s * price;
        return cust;
    }
}