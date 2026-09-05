from abc import ABC, abstractmethod
import threading
import time
import asyncio
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TerminalError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Ошибка: '{value}' нельзя преобразовать в число.")

class OverchargeError(Exception):
    def __init__(self, charge):
        super().__init__(f"Нельзя зарядить мышь на {charge}%, это выше 100!")


def decorator_register(func):
    def wrapper():
        print("Отработано взаимодействие между двумя мышами!")
        func()
    return wrapper

def check_charge(func):
    def wrapper(self, dpi, *args, **kwargs):
        if self.charge == 0:
            print('Сначала заряди мышку!')
            self.log("Error changing DPI.")
        else: return func(self, dpi, *args, **kwargs)
    return wrapper

def is_charge_valid(func):
    def wrapper(self, charge, *args, **kwargs):
        if charge < 0 or charge > 100:
            print('Неверный ввод зарядки!')
            self.log("Error charging.")
        else: return func(self, charge, *args, **kwargs)

class Meta1(type):
    def __new__(cls, name, bases, dct):
        def click(self):
            print('click!')
        dct['click'] = click
        return super().__new__(cls, name, bases, dct)

class LoggingMixin:
    def log(self, message):
        print(f"LOG: {message}")
    def error(self, message):
        print(f"ERROR: {message}")

class MouseButton(metaclass=Meta1):
    def __init__(self):
        pass

class Mouse(ABC, LoggingMixin):
    @abstractmethod
    def __init__(self, color, model, dpi, charge):
        try:
            self.__color = color
            self.__model = model 
            self.__dpi = dpi
            self.__charge = charge
            self.mousebutton = MouseButton()
        except:
            self.error("Ошибка инициализации!")
    @decorator_register
    def __add__(self, other):
        if isinstance(other, Mouse):
            return Mouse(self.__color + "-" + other.__color, "Гибрид <" + self.__model + " + " + other.__model + ">", self.__dpi + other.__dpi, self.__charge + other.__charge)
    @decorator_register
    def __sub__(self, other):
        if isinstance(other, Mouse):
            return Mouse("-", "кучка деталей от " + self.__model + " и " + other.__model, 0, 0)
    @check_charge
    def Change_dpi(self, dpi):
        try:
            self.__dpi = dpi
            print('Установлен dpi:', dpi)
            self.log("DPI changed successfully.")
        except:
            self.error("Ошибка выставления dpi!")
    def Use(self):
        self.__charge = 0
        self.mousebutton.click()
        print('Мышка активно использовалась, теперь она разряжена')
        self.log("Used successfully.")
    def Charge(self, charge):
        if charge > 100:
            raise OverchargeError(charge)
        try:
            self.__charge = charge
            print(f'Мышь заряжена на {charge}%')
            self.log("Charged successfully.")
        except:
            self.error("Ошибка зарядки!")
    def Info(self):
        print('Цвет:',self.__color, 'Модель:', self.__model, 'dpi:', self.__dpi, 'Заряд:', self.__charge)
        self.log("Displayed info successfully.")

class GamingMouse(Mouse):
    def __init__(self, color, model, dpi, charge):
        super().__init__(color, model, dpi, charge)
        self.design = 'Gaming'
    def set_design(self, design):
        self.design = design
        self.log("Design changed successfully.")
    def get_design(self):
        print(self.design)
        self.log("Displayed design successfully.")
    def play(self):
        print('Игра!')
        self.Use()
        self.log("Played successfully.")

class OfficeMouse(Mouse):
    def __init__(self, color, model, dpi, charge):
        super().__init__(color, model, dpi, charge)
        self.dirty = True
    def clear(self):
        print('Вы почистили мышь!')
        self.dirty = False
        self.log("Cleaned successfully.")
    def Work(self):
        print('работа...')
        self.log("Worked successfully.")
        self.Use()
        print('К тому же, мышь испачкалась!')
        self.dirty = True

class Terminal(LoggingMixin):
    def __init__(self):
        self.log("Добро пожаловать!")
        self.__mouses = []
        self.charge = 100
        self.conn = sqlite3.connect("C:/Users/seray/Desktop/учёба/прога/весна/дз/mouses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS mouses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            color TEXT,
            model TEXT,
            dpi INTEGER,
            charge INTEGER,
            extra TEXT
        )''')   
        self.conn.commit()
        self.load_mouses_from_db()
    def save_mouse_to_db(self, mouse):
        if isinstance(mouse, GamingMouse):
            extra = mouse.design
            type_ = "GamingMouse"
        elif isinstance(mouse, OfficeMouse):
            extra = str(mouse.dirty)
            type_ = "OfficeMouse"
        else:
            extra = "-"
            type_ = "Mouse"
        self.cursor.execute("INSERT INTO mouses (type, color, model, dpi, charge, extra) VALUES (?, ?, ?, ?, ?, ?)", 
                        (type_, mouse._Mouse__color, mouse._Mouse__model, mouse._Mouse__dpi, mouse._Mouse__charge, extra))
        self.conn.commit()
    def load_mouses_from_db(self):
        self.cursor.execute("SELECT type, color, model, dpi, charge, extra FROM mouses")
        rows = self.cursor.fetchall()
        for row in rows:
            type_, color, model, dpi, charge, extra = row
            if type_ == "GamingMouse":
                mouse = GamingMouse(color, model, int(dpi), int(charge))
                mouse.set_design(extra)
            elif type_ == "OfficeMouse":
                mouse = OfficeMouse(color, model, int(dpi), int(charge))
                mouse.dirty = (extra == "True")
            self.__mouses.append(mouse)
    def add_mouse(self):
        a = TkInfoGetter()
        res = list(a.rtrn().values())
        choice = res[0]
        col = res[1]
        mod = res[2]
        dpi = res[3]
        charge = res[4]
        if choice == 1:
            m = GamingMouse(col, mod, int(dpi), int(charge))
        elif choice == 2:
            m = OfficeMouse(col, mod, int(dpi), int(charge))
        else:
            self.log("Ошибка. Возможно, вы некорректно указали тип мыши")
            return
        self.__mouses.append(m)
        self.save_mouse_to_db(m)
    def show_mouses(self):
        print("Каталог мышей:")
        for i in range(len(self.__mouses)):
            self.__mouses[i].Info()
    def hybrid(self):
        self.show_mouses()
        i1, i2 = map(int, input('Введите номера мышей, которые хотите совместить: ').split())
        try:
            m1 = self.__mouses[i1 - 1]
            m2 = self.__mouses[i2 - 1]
            new_mouse = asyncio.run(hybrid_async(m1, m2))
            self.__mouses.append(new_mouse)
            self.__mouses.pop(max(i1, i2) - 1)
            self.__mouses.pop(min(i1, i2) - 1)
            self.log('Создан гибрид успешно.')
        except Exception as e:
            self.error(f'Ошибка совмещения мышей! {e}')
    def exxit(self):
        exit()

class TkInfoGetter:
    def __init__(self):
        self.res = {}
        self.root = tk.Tk()
        self.root.title("Ввод данных")
        self.root.geometry("400x300")
        self.mouse_type = tk.IntVar(value=1)
        ttk.Label(self.root, text="Тип мыши:").grid(row=0, column=0, sticky='w')
        ttk.Radiobutton(self.root, text="Игровая", variable=self.mouse_type, value=1).grid(row=0, column=1, sticky='w')
        ttk.Radiobutton(self.root, text="Офисная", variable=self.mouse_type, value=2).grid(row=0, column=2, sticky='w')
        ttk.Label(self.root, text="Цвет:").grid(row=1, column=0, sticky='w')
        self.color_entry = ttk.Entry(self.root)
        self.color_entry.grid(row=1, column=1, columnspan=2, sticky='we')
        ttk.Label(self.root, text="Модель:").grid(row=2, column=0, sticky='w')
        self.model_entry = ttk.Entry(self.root)
        self.model_entry.grid(row=2, column=1, columnspan=2, sticky='we')
        ttk.Label(self.root, text="DPI:").grid(row=3, column=0, sticky='w')
        self.dpi_entry = ttk.Entry(self.root)
        self.dpi_entry.grid(row=3, column=1, columnspan=2, sticky='we')
        ttk.Label(self.root, text="Заряд:").grid(row=4, column=0, sticky='w')
        self.charge_entry = ttk.Entry(self.root)
        self.charge_entry.grid(row=4, column=1, columnspan=2, sticky='we')
        submit_btn = ttk.Button(self.root, text="Подтвердить", command=self.submit)
        submit_btn.grid(row=5, column=0, columnspan=3, pady=10)
        self.root.mainloop()
    def submit(self):
        self.res = {'type': self.mouse_type.get(), 'color': self.color_entry.get(), 'model': self.model_entry.get(), 'dpi': self.dpi_entry.get(), 'charge': self.charge_entry.get()}
        if not all(self.res.values()):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return
        try:
            self.res['dpi'] = int(self.res['dpi'])
            self.res['charge'] = int(self.res['charge'])
        except ValueError:
            messagebox.showerror("Ошибка", "DPI и заряд должны быть числами!")
            return
        self.root.quit()
    def rtrn(self):
        return self.res

def terminal_discharge(term):
    while True:
        time.sleep(5)
        term.charge -= 1
        if term.charge <= 0:
            print("[Терминал] Заряд исчерпан. Завершение работы.")
            exit()

async def hybrid_async(mouse1, mouse2):
    print("Создание гибрида начато...")
    await asyncio.sleep(2)
    print("Гибрид готов!")
    return mouse1 + mouse2


A = Terminal()
discharge_thread = threading.Thread(target=terminal_discharge, args=(A,), daemon=True)
discharge_thread.start()
while True:
    print("[Терминал] 1 - добавить мышь, 2 - показать список мышей, 3 - создать гибрид, 0 - выход")
    try:
        s = input("[Терминал] Что вы хотите сделать?... ")
        try:
            ch = int(s)
        except ValueError:
            raise TerminalError(s)
    except TerminalError as err:
        print(err)
        continue
    if ch == 1:
        A.add_mouse()
    elif ch == 2:
        A.show_mouses()
    elif ch == 3:
        pass
    elif ch == 0:
        A.exxit()


