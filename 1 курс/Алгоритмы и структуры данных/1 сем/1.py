# n log n

n=int(input())
a=list(map(int, input().split()))
a.sort()
for i in range(n-1):
    if a[i+1]-a[i]!=1:
        print(a[i+1]-1)
        break

# n
'''
n=int(input())
a=list(map(int, input().split()))
b=[0]*n
for i in range(n):
    b[a[i]-1]+=1
print(b.index(0)+1)
'''
# n^2
'''
n=int(input())
a=list(map(int, input().split()))
c=False
while c!=True:
    c=True
    for i in range(n-1):
        if a[i+1]<a[i]:
            c=False
            a[i], a[i+1] = a[i+1], a[i]
for i in range(n-1):
    if a[i+1]-a[i]!=1:
        print(a[i+1]-1)
        break
'''