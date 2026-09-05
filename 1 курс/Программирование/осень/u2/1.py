name = input('Введите имя: ')
pol = input('М/Ж: ')
old = int(input('Возраст: '))
if pol == 'М':
    first = 'Его'
    second = 'Ему'
else:
    first = 'Её'
    second = 'Ей'
if (11 <= old % 100 <=14) or old % 10 not in [1,2,3,4]:
    third = 'лет'
elif old % 10 in [2,3,4]:
    third = 'года'
else:
    third = 'год'
print(f'{first} зовут {name}. {second} {old} {third}')