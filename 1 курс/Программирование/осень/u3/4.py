a=input()
points=0
while a!='STOP':
    x,y=map(float,a.split())
    if x==0 or y==0:
        a=input()
        continue
    if x>0:
        if y>0: points+=1
        else: points+=4
    else:
        if y>0: points+=2
        else: points+=3
    a=input()
print(points)
    