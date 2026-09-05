time=int(input('Введите секунды: '))
day=time//86400
time=time%86400
hour=time//3600
time=time%3600
mn=time//60
time=time%60
print(f'{day}:{hour}:{mn}:{time}')