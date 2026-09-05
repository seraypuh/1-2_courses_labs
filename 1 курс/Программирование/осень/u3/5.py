from random import *
import keyboard
import time
def f(x):
    global running
    running=False

running=True
while running:
    print("игра началась!")
    ran=randint(1,100)
    att=0
    while att<10:
        att+=1 
        try:
            a=int(input())
        except:
            print('это не число!')
            a=int(input())
        if a==ran:
            print('Верно!')
            break
        elif a>ran:
            print('Меньше!')
        else:
            print('Больше!')
    if att>=10:
        print('Вы проиграли. Нажмите Enter, чтобы сыграть ещё раз, Q чтобы выйти...')
        keyboard.on_press_key('q', f)
        time.sleep(3)
    else: break
print('Игра закончена')