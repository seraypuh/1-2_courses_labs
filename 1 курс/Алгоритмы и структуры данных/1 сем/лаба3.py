# блочная сортировка
'''
numbers=list(map(int,input().split()))
blocks=[[],[],[],[],[]]
for i in range(len(numbers)):
    blocks[(numbers[i]//20)].append(numbers[i])
res=[]
for i in range(len(blocks)):
    res+=sorted(blocks[i])
print(*res)
'''
# пирамидальная сортировка
'''
a=list(map(int,input().split()))
size=len(a)
for i in range(size//2-1,-1,-1):
    mx=i
    l=2*i+1
    r=2*i+2
    if l<size and a[l]>a[mx]:
        mx=l
    if r<size and a[r]>a[mx]:
        mx=r
    if mx!=i:
        a[i],a[mx]=a[mx],a[i]
        j=mx
        while j<size//2:
            mx=j
            l=2*j+1
            r=2*j+2
            if l<size and a[l]>a[mx]:
                mx=l
            if r<size and a[r]>a[mx]:
                mx=r
            if mx!=j:
                a[j],a[mx]=a[mx],a[j]
                j=mx
            else: break
for i in range(size-1,0,-1):
    a[i],a[0]=a[0],a[i]
    mx=0
    j=0
    while j<i//2:
        mx=j
        l=2*j+1
        r=2*j+2
        if l<i and a[l]>a[mx]:
            mx=l
        if r<i and a[r]>a[mx]:
            mx=r
        if mx!=j:
            a[j],a[mx]=a[mx],a[j]
            j=mx
        else: break
print(a)
'''
# сортировка слиянием
'''
def sorting(a):
    if len(a)<2: return a
    l=sorting(a[:len(a)//2])+[999999999]
    r=sorting(a[len(a)//2:])+[999999999]
    res=[0]*len(a)
    cl=0
    cr=0
    cres=0
    while len(l)-1>cl or len(r)-1>cr:
        if l[cl]<=r[cr]:
            res[cres]=l[cl]
            cl+=1
        else:
            res[cres]=r[cr]
            cr+=1
        cres+=1
    return res
a=list(map(int,input().split()))
print(sorting(a))
'''