day1=int(input())
res=int(input())
k=1
if day1<=0:
    print('неверный ввод')
else:
    while day1<res:
        k+=1
        day1=day1*1.1
    print(k)