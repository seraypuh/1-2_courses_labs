from abc import ABC, abstractmethod
class Country(ABC):
    def __init__(self, capital, population):
        self.__capital = capital
        self.__population = population
    def get_population(self):
        return self.__population
    def get_capital(self):
        return self.__capital
    def set_population(self, population):
        if population >= 0:
            self.__population = population
        else: print('неверное значение')
    def set_capital(self, capital):
        self.__capital = capital
    @abstractmethod
    def Border(self):
        pass

class Russia(Country):
    def __init__(self, capital, population):
        super().__init__(capital, population)
        self.__Border = 'N/A'
    def Border(self):
        return self.__Border
    def set_Border(self, border):
        self.__Border = border
    def Info(self):
        print('Население:', self.__population, 'Столица:', self.__capital, 'Границы', self.__Border)

class Canada(Country):
    def __init__(self, capital, population):
        super().__init__(capital, population)
        self.__Border = 'N/A'
    def Border(self):
        return self.__Border
    def set_Border(self, border):
        self.__Border = border
    def Info(self):
        print('Население:', self.__population, 'Столица:', self.__capital, 'Границы:', self.__Border)

class Germany(Country):
    def __init__(self, capital, population):
        super().__init__(capital, population)
        self.__Border = 'N/A'
    def Border(self):
        return self.__Border
    def set_Border(self, border):
        self.__Border = border
    def Info(self):
        print('Население:', self.get_population(), 'Столица:', self.get_capital(), 'Границы', self.Border())

a = Germany('Berlin', 80000000)
a.set_Border('Closed')
a.Info()