using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Gamer
{
    string Name;
    IgralnayaKost seans;
    public Gamer(string name)
    {
        Name = name;
        seans = new IgralnayaKost();
    }
    public int SeansGame()
    {
        return seans.random();
    }
    public override string ToString()
    {
        return Name;
    }
}