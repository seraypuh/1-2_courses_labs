class Car:
    def __init__(self):
        self.color = 'N/A'
        self.type = 'N/A'
        self.year = -1
        self.start = False
    def Start(self):
        if self.start == False:
            self.start = True
            print('Автомобиль заведён')
        else:
             print('Автомобиль уже заведён!')
    def Stop(self):
        if self.start == True:
            self.start = False
            print('Автомобиль заглушен')
        else:
             print('Автомобиль уже заглушен!')
    def Year(self, year):
        if year<1886 or year>2025:
            print('Неверный год!')
        else:
            self.year = year
    def Color(self, color):
        self.color = color
    def Type(self, t):
        self.type = t
    def Info(self):
        print('Цвет:', self.color)
        print('Тип:', self.type)
        print('Год Выпуска:', self.year)
a = Car()
a.Start()
a.Start()
a.Stop()
a.Year(int(input()))
a.Color(input())
a.Type(input())
a.Info()