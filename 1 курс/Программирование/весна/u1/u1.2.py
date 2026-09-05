class Triangle:
    def __init__(self, a, b, c):
        if a+b>c and a+c>b and b+c>a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Ошибка задания треугольника!')
            self.__init__(int(input()), int(input()), int(input()))
    def Area(self):
        p = (self.a+self.b+self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
a,b,c = map(int, input().split())
t = Triangle(a,b,c)
print(t.Area())