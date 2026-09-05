h1,m1 = map(int, input('Отправление: ').split(':'))
h2,m2 = map(int, input('Прибытие: ').split(':'))
if h2 < h1: hh = h2 + 23 - h1
else: hh = h2 - h1
if m2 < m1: mm = m2 + 60 - m1
else: mm = m2 - m1
print(f'{hh}:{mm}')