class Mouse:
    def __init__(self, color, model, dpi, charge):
        self.color = color
        self.model = model
        self.dpi = dpi
        self.charge = charge
    def Change_dpi(self, dpi):
        if self.charge == 0:
            print('Сначала заряди мышку!')
        else:
            self.dpi = dpi
            print('Установлен dpi:', dpi)
    def Use(self):
        self.charge = 0
        print('Мышка активно использовалась, теперь она разряжена')
    def Charge(self, charge):
        if charge < 0 or charge > 100:
            print('Неверный ввод зарядки!')
        else:
            self.charge = charge
            print(f'Мышь заряжена на {charge}%')
    def Info(self):
        print('Цвет:',self.color, 'Модель:', self.model, 'dpi:', self.dpi, 'Заряд:', self.charge)
a = Mouse(input(), input(), int(input()), int(input()))
a.Change_dpi(8000)
a.Use()
a.Charge(98)
a.Info()