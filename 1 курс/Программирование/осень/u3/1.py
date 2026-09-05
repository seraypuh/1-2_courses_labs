def f(x):
    a=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            a.add(i)
            a.add(x//i)
    return a
a=int(input())
b=[]
for i in range(1,a+1):
    if len(f(i))==2: b.append(i)
print(b)
