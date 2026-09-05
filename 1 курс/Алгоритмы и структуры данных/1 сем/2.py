def spl(n):
    m=len(n)//2
    return n[:m],n[m:]
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
c=True
for i in range(n-1):
    p1,p2 = spl(a[n-1-i])
    p2=p2[::-1]
    if p2!=p1:
        c=False
        break
print(c)