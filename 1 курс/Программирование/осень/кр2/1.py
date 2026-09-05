def f(a):
    b=[]
    for i in range(len(a)):
        try:
            float(a[i])
            b.append(float(a[i]))
            if float(a[i])<=0:
                print('Некорректное время')
                return 0
        except: continue
    b=list(sorted(b))
    sr=round((sum(b)/len(b)),2)
    print('Средний результат:', sr)
    print('Три лучших времени:',b[0],b[1],b[2])
a=list(input('Введите результаты: ').split())
f(a)

