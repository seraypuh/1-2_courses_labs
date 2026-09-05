using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class IgralnayaKost
{
    Random r;
    public IgralnayaKost()
    {
        r = new Random();
    }
    public int random()
    {
        int res = r.Next(6) + 1;
        return res;
    }
}