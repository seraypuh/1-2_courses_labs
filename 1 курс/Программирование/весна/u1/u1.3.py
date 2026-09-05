class Coffee:
    def __init__(self, db=None):
        self.db = db
    def show_my_drink(self):
        if self.db != '':
            print(f'Кофе и {self.db}')
        else:
            print('Чёрный кофе')
c = Coffee(input())
c.show_my_drink()