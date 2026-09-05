def f1(x0,s,x):
    if s==0: return x
    elif s>0:
        x=x*x0
        return f1(x0,s-1,x)
    else:
        x=x*(1/x0)
        if x<=1:
            return f1(x0,s+1,x)
        else:
            return f1(x0,s+1,1/x)
def f2(x,s): return x**s
def f():
    try:
        x0,s=list(map(float,input('Введите число и степень: ').split()))
    except:
        print('Некорректный ввод')
    print(f1(x0,s,1))
    print(f2(x0,s))
f()