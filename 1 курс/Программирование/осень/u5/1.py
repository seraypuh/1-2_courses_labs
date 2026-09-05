def X(a,b,c):
    D=b**2-4*a*c
    if D<0: return "Нет решений в R"
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
    return x1, x2
def user(s):
    if s=='STOP': return 0
    try:
        a,b,c=map(float,s.split())
    except:
        print('Введите числа, а не текст!')
        s=input('Введите числа: ')
        return user(s)
    print('Корни уравнения:', X(a,b,c))
    s=input('Введите числа: ')
    return user(s)
user(input('Введите числа: '))