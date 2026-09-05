from math import *
a,b,c = map(int,input("Введите стороны треугольника (через пробел): ").split())
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'Площадь треугольника = {s}')
else:
    print('это не треугольник!')
