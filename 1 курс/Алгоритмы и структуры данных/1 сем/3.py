def podstroki(s):
    a = set()
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            a.add(s[i:j])
    return a
s=input()
n=int(input())
a=list(podstroki(s))
b=[]
for i in range(len(a)):
    if s.count(a[i]) == 1:
        b.append(a[i])
b.sort()
b=sorted(b, key=len)
c=[]
for i in range(len(b)):
    if len(b[i]) == len(b[0]):
        c.append(b[i])
print(c)
print(c[n-1])