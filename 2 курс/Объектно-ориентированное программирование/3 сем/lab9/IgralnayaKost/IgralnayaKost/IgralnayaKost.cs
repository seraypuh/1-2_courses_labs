using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class IgralnayaKost
{
    Random r;
    public event Action MaxScore;
    public IgralnayaKost()
    {
        r = new Random();
    }
    public int random()
    {
        int res = r.Next(6) + 1;
        if (res == 6)
        {
            MaxScore?.Invoke();
        }
        return res;
    }
}