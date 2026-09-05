def calc(a):
    try: 
        b=eval(a)
        return b
    except: return 'Некорректный ввод'
def user():
    a=input('Введите расчёт (STOP для остановки): ')
    if a=='STOP':
        return 0
    b=calc(a)
    try:
        float(b)
        b=round(b,2)
        print(a,'=',b,sep='')
        return user()
    except:
        print(b)
        return user()
user()