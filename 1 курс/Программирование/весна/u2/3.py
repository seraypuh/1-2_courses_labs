class Cat:
    def __init__(self, name, age):
        if age > 19 or age < 0:
            raise ValueError('Неверный возраст!')
        self.__name = name
        self.__age = age
        self.__fur = 'N/A'
    def set_info(self, name, age):
        self.__name = name
        self.__age = age

class Sfinks(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__fur = 'Лысый'
    def Hunt(self):
        print('Охота')
    def Info(self):
        print(self._Cat__name)
        print(self._Cat__age)
        print(self.__fur)

class MeinKun(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__fur = 'длинная'
    def CatchMouse(self):
        print('Ловля крыс')
    def Info(self):
        print(self._Cat__name)
        print(self._Cat__age)
        print(self.__fur)

class Korat(Cat): 
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__fur = 'средняя'
    def Play(self):
        print('Игра')
    def Info(self):
        print(self._Cat__name)
        print(self._Cat__age)
        print(self.__fur)
a=Sfinks('vasya', 17)
a.Info()