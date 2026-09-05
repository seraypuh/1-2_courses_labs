# 1
'''
a=input('введите телестих ')
name=''
while a!='':
    a=a.replace('.','').replace(',','').replace('!','').replace('?','').replace(' ','').replace('-','').replace('(','').replace(')','')
    name=name+a[-1]
    a=input()
print(name)
'''
# 2
'''
product=[]
cost=[]
price=[]
t=input("введите продукт и цену: ")
while t!='':
    try: 
        a,b=t.split()
        int(b)
    except:
        print('ошибка вводи нормально')
        t=input("введите продукт и цену: ")
        continue
    product.append(a)
    if int(b)<=0 or int(b)>=100000:
        print("что с ценой?")
        t=input("введите продукт и цену: ")
        continue
    cost.append(int(b))
    price.append(round(int(b)*1.15, 2))
    t=input("введите продукт и цену: ")
zipped=list(zip(product,cost,price))
f=open('C:/Users/Serega/Desktop/учёба/прога/кр1/2.txt', "w+")
for i in range(len(zipped)):
    print(*zipped[i])
    f.write(zipped[i][0]+' '+str(zipped[i][1])+' '+str(zipped[i][2])+'\n')
f.close()
'''

# 3
'''
from random import *
a=[]
for i in range(20): a.append(randint(1,20))
m=12
b=[]
for i in range(20):
    if a[i]>m: b.append('High')
    elif a[i]<m: b.append('Low')
    else: b.append('Equal')
names=['Яна', 'Иван', 'Мария', 'Анастасия', 'Дмитрий', 'Сергей', 'Алексей', 'Владимир', 'Екатерина', 'Ольга', 'Татьяна', 'Елена', 'Юлия', 'Ирина', 'Светлана', 'Анна', 'Виктория', 'Ксения', 'Полина', 'Никита', 'Максим']
ak=[]
other=[]
for i in range(len(names)):
    if ord('А')<=ord(names[i][0])<=ord('К'):
        ak.append(names[i])
    else: other.append(names[i])
print(*a)
print(*b)
print(*names)
print(*ak)
print(*other)
'''

# 4

f=open('C:/Users/Serega/Desktop/учёба/прога/кр1/4.txt', "w+")
a=list(map(float,input("Введите числа ").split()))
for i in range(len(a)):
    if a[i]<10: a[i]=round(a[i]*1.12, 2)
    elif a[i]>10: a[i]=round(a[i]*0.25, 2)
a=sorted(a)
print(*a)
s=''
for i in range(len(a)): s=s+str(a[i])+' '
f.write(s)
f.close()
