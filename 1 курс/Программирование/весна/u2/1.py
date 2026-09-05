class Pupil:
    def __init__(self):
        self.__name = 'Radomir'
        self.__age = 8
        self.__classNumber = '1-A'
    def get_info(self):
        print('name:', self.__name)
        print('age:', self.__age)
        print('classNumber:', self.__classNumber)
    def set_info(self, name, age, classNumber):
        self.__name = name
        self.__age = age
        self.__classNumber = classNumber
a=Pupil()
a.set_info('abc', 6, '3-B')
a.get_info()