def shifr(s,k):
    a=''
    for i in s:
        a+=chr(ord(i)^k)
    return a
def user():
    s=input('Введите код для шифрования (STOP для остановки): ')
    if s=="STOP": return 0
    k=input('Введите ключ для шифрования: ')
    try:
        int(k)
    except:
        print('Ключ - не целое число!')
        return user()
    if k.isdigit==False:
        print('Ключ - не целое число!')
        return user()
    a=shifr(s,int(k))
    print('Зашифровано:',a)
    b=shifr(a,int(k))
    print('Расшифровано:',b)
    return user()
user()