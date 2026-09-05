def f(a1: str,b1: str):
    a=int(a1)
    b=int(b1)
    if len(a1)!=9 and len(b1)!=2:
        return False
    if '000' in a1 or '111' in a1 or '222' in a1 or '333' in a1 or '444' in a1 or '555' in a1 or '666' in a1 or '777' in a1 or '888' in a1 or '999' in a1:
        return False
    a2=a1[::-1]
    s=int(a2[0])*1 + int(a2[1])*2 + int(a2[2])*3 + int(a2[3])*4 + int(a2[4])*5 + int(a2[5])*6 + int(a2[6])*7 + int(a2[7])*8 + int(a2[8])*9
    if s<100:
        if b==s:
            return True
        else: return False
    if s==100 or s==101:
        if b1=='00':
            return True
        else: return False
    if s>101:
        s=s%101
        if s<100:
            if b==s: return True
            else: return False
        if s==100:
            if b1=='00': return True
            else: return False
try:
    a1,b1=input("Введите снилс: ").split()
    print(f(a1,b1))
except:
    print('Ошибка ввода')