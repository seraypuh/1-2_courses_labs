# O(3n) - алгоритм выводит сумму, среднее арифметическое и среднее геометрическое чисел в массиве
'''def f(mass):
    s=0
    a=0
    g=1
    for i in range(len(mass)):
        s+=mass[i]
    for i in range(len(mass)):
        a+=mass[i]
    a=a/len(mass)
    for i in range(len(mass)):
        g=g*mass[i]
    g=g**(1/len(mass))
    return s,a,g
a=list(map(int,input("Введите массив: ").split()))
print(f(a))'''
# O(nlogn) - алгоритм ищет номер загаданной буквы в английском алфавите
'''def f(x):
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    low = 0
    high = len(alph) - 1
    mid = len(alph) // 2
    while alph[mid] != x and low <= high:
        if x > alph[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return('нет такой буквы!')
    else:
        return mid+1
print(f(input()))'''
# O(n!) - алгоритм находит все варианты расположения букв в слове
'''from itertools import *
word=input()
for x in product(word,repeat=len(word)):
    s=''.join(x)
    print(s)'''
# O(n^3) - алгоритм ищет тройку чисел среди заданных, равную заданному числу в сумме
'''n=int(input('Введите число: '))
a=list(map(int,input("Введите числа для поиска: ").split()))
found=False
for i in range(len(a)-2):
    if not found:
        for j in range(i+1,len(a)-1):
            if not found:
                for k in range(j+1,len(a)):
                    if a[i]+a[j]+a[k]==n:
                        print(a[i],a[j],a[k])
                        found=True
                        break
if not found: 
    print('Нет такой тройки чисел!')'''
# O(3log(n)) - алгоритм находит 3 спрятанных еденицы в массиве и выводит их индексы
'''a=list(map(str,input('Введите ряд нулей и едениц (еденицы 3, остальное нули): ').split()))
for i in range(3):
    if a.count('1')==3-i:
        low = 0
        high = len(a) - 1
        mid = len(a) // 2
        x=a.index('1')
        while mid != x and low <= high:
            if x > mid:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            print('нет еденицы!')
        else:
            print(mid)
        a[mid]='0'
    else: 
        print("здесь нет трёх едениц!")
        break'''