from math import pi
def circle(r): return pi*r**2
def rectangle(a,b): return a*b
def check(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else: return False
def triangle(a,b,c):
    p=0.5*(a+b+c)
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
def f():
    print('Выберите фигуру:')
    print('1. Круг  2. Прямоугольник  3. Треугольник')
    choice=input()
    if choice not in ['1','2','3']:
        print('Вводи нормально!')
        return f()
    i=int(choice)
    if i==1:
        r=input('Введите радиус круга: ')
        try: r1=float(r)
        except: 
            print('Вводи нормально!')
            return f()
        if r1<=0:
            print('Вводи нормально!')
            return f()
        print('Площадь круга:', circle(r1))
    elif i==2:
        s=input('Ввеите стороны прямоугольника: ') 
        try: a,b=map(float,s.split())
        except:
            print('Вводи нормально!')
            return f()
        if a<=0 or b<=0:
            print('Вводи нормально!')
            return f()
        print('Площадь прямоугольника:', rectangle(a,b))
    elif i==3:
        s=input('Ввеите стороны треугольника: ') 
        try: a,b,c=map(float,s.split())
        except:
            print('Вводи нормально!')
            return f()
        if a<=0 or b<=0 or c<=0:
            print('Вводи нормально!')
            return f()
        if check(a,b,c):
            print('Площадь треугольника:', triangle(a,b,c))
        else: print('Такого треугольника не существует')
    q=input('Проолжить? YES для продолжения ')
    if q=='YES': f()
f()