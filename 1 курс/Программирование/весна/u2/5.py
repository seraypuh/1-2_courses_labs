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

class GamingMouse(Mouse):
    def __init__(self, color, model, dpi, charge):
        super().__init__(color, model, dpi, charge)
        self.design = 'Gaming'
    def set_design(self, design):
        self.design = design
    def get_design(self):
        print('design')
    def play(self):
        print('Игра!')
        self.Use()

class OfficeMouse(Mouse):
    def __init__(self, color, model, dpi, charge):
        super().__init__(color, model, dpi, charge)
        self.dirty = True
    def clear(self):
        print('Вы почистили мышь!')
        self.dirty = False
    def Work(self):
        print('работа...')
        self.Use()
        print('К тому же, мышь испачкалась!')
        self.dirty = True
a= GamingMouse('black', 'logitech', 1000, 100)
a.play()
a.Info()

b = OfficeMouse('black', 'logitech', 1000, 100)
b.clear()
b.Work()
