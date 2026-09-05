class Doctor:
    def __init__(self, age):
        self.__age = 25
    def change(self, age):
        if age >= 25:
            self.__age = age
        else:
            print('Ошибка задания возраста!')

class Pediatr(Doctor):
    def __init__(self, age):
        super().__init__(age)
        self.__name = 'N/A'
    def change(self, age, name):
        if age >= 25:
            self.__age = age
            self.__name = name
        else:
            print('Ошибка задания возраста!')
    def Info(self):
        print('возраст:', self.__age)
        print('имя:', self.__name)


class Okulist(Doctor):
    def __init__(self, age):
        super().__init__(age)
        self.__exp = 0
    def change(self, age, exp):
        if age >= 25:
            self.__age = age
            self.__exp = exp
        else:
            print('Ошибка задания возраста!')
    def Info(self):
        print('возраст:', self.__age)
        print('стаж:', self.__exp)

class Dentist(Doctor):
    def __init__(self, age):
        super().__init__(age)
        self.__zp = 0
    def change(self, age, zp):
        if age >= 25:
            self.__age = age
            self.__zp = zp
        else:
            print('Ошибка задания возраста!')
    def Info(self):
        print('возраст:', self.__age)
        print('зарплата:', self.__zp)

a = Dentist(38)
a.change(39, 2500000)
a.Info()
