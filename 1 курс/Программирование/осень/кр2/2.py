def f():
    try:
        a=list(map(float,input().split()))
    except:
        print('Не числовые значения')
        return 0
    b=[]
    c=[]
    for i in range(len(a)):
        if a[i]<0: b.append(a[i])
        else: c.append(a[i])
    b=list(reversed(list(sorted(b))))
    c=list(sorted(c))
    return tuple([b,c])
print(f())
