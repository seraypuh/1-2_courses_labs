day, month = map(int, input().split())
if (month==2 and day <= 29) or (month in [1,3,5,7,8,10,12] and day <= 31) or (month in [4,6,9,11] and day <=30):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = days[month - 1] - day
    for i in range(month,12):
        count += days[i]
    print('До нового года осталось: ', count, " дней")
else: print('Неверная дата!')