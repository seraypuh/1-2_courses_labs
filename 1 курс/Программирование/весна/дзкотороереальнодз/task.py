from abc import ABC, abstractmethod
import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
import sys
from io import StringIO
import io
from unittest.mock import patch

class LoggingMixin:
    def error(self, message):
        messagebox.showwarning("Ошибка", message)
    def log(self, message):
        messagebox.showinfo("LOG", message)

class transport(ABC, LoggingMixin):
    def __init__(self, length, width, height):
        self.__height = height
        self.__load_capacity = -1
        self.__length = length
        self.__width = width
        self.__type = 'N/A'
    def show_load_capacity(self):
        return self.__load_capacity
    def show_size(self):
        return [self.__length, self.__width, self.__height, self.__load_capacity]
    def show_type(self):
        return self.__type

class Gazel(transport):
    def __init__(self, length, width, height):
        try:
            super().__init__(length, width, height)
            self.__type = "Gazel"
            self.__load_capacity = 2
            self.__length = 3
            self.__width = 2
            self.__height = height
            if (not(1.7 <= self.__height <= 2.2)): a = 0/0
        except:
            self.error(f"Некорректная высота. Для {self.__type} допустима от 1.7 до 2.2")
            return

class Bichok(transport):
    def __init__(self, length, width, height):
        try:
            super().__init__(length, width, height)
            self.__type = "Bichok"
            self.__load_capacity = 3
            self.__length = length
            self.__width = width
            self.__height = height
            if (not(2 <= self.__height <= 2.4)) or (not(2 <= self.__width <= 2.2)) or (not(4.2 <= self.__length <= 5)): a = 0/0
        except:
            self.error(f"Некорректные габариты. Для {self.__type} допустимо: Длина 4.2 - 5; Ширина 2 - 2.2; Высота 2 - 2.4.")
            return

class MAN10(transport):
    def __init__(self, length, width, height):
        try:
            super().__init__(length, width, height)
            self.__type = "MAN10"
            self.__load_capacity = 10
            self.__length = length
            self.__width = 2.45
            self.__height = height
            if (not(2.3 <= self.__height <= 2.7)) or (not(6 <= self.__length <= 8)): a = 0/0
        except:
            self.error(f"Некорректные габариты. Для {self.__type} допустимо: Длина 6 - 8; Ширина 2.45; Высота 2.3 - 2.7.")
            return

class Fura(transport):
    def __init__(self, length, width, height):
        try:
            super().__init__(length, width, height)
            self.__type = "Fura"
            self.__load_capacity = 20
            self.__length = 13.6
            self.__width = 2.46
            self.__height = height
            if (not(2.5 <= self.__height <= 2.7)): a = 0/0
        except:
            self.error(f"Некорректная высота. Для {self.__type} допустима от 2.5 до 2.7")
            return

class Cargo:
    def __init__(self, a, b, c, weight):
        self.a = a
        self.b = b
        self.c = c
        self.weight = weight
    def __add__(self, other):
        if isinstance(other, Cargo):
            return Cargo(self.a + other.a, self.b + other.b, self.c + other.c, self.weight + other.weight)

class Application:
    def __init__(self, car, a, b, c, weight):
        self.car = car 
        self.a = a
        self.b = b
        self.c = c
        self.weight = weight
        
class Terminal(LoggingMixin):
    def __init__(self):
        self.log("Добро пожаловать!")
        self.conn = sqlite3.connect('C:/Users/seray/Desktop/учёба/прога/весна/дзкотороереальнодз/dz.db')
        self._create_tables()
    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            a REAL NOT NULL,
            b REAL NOT NULL,
            c REAL NOT NULL,
            weight REAL NOT NULL,
            is_available BOOLEAN DEFAULT 1
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER NOT NULL,
            a REAL NOT NULL,
            b REAL NOT NULL,
            c REAL NOT NULL,
            weight REAL NOT NULL,
            FOREIGN KEY (car_id) REFERENCES cars (id)
        )
        ''')
        self.conn.commit()
    def add_transport(self):
        choice = int(input("Выберите траспорт для добавления: 1 - Газель, 2 - Бычок, 3 - MAN10, 4 - Фура: "))
        a, b, c = map(int, input("Выберите габариты: ").split())
        if choice == 1:   
            tr = 2
            if (not(1.7 <= c <= 2.2)) or (not(2 <= b <= 2)) or (not(3 <= a <= 3)):
                self.log("Некорректные габариты.")
                return
        elif choice == 2: 
            tr = 3
            if (not(2 <= c <= 2.4)) or (not(2 <= b <= 2.2)) or (not(4.2 <= a <= 5)):
                self.log("Некорректные габариты.")
                return
        elif choice == 3: 
            tr = 10
            if (not(2.3 <= c <= 2.7)) or (not(2.45 <= b <= 2.45)) or (not(6 <= a <= 8)):
                self.log("Некорректные габариты.")
                return
        elif choice == 4: 
            tr = 20
            if (not(2.5 <= c <= 2.7)) or (not(2.46 <= b <= 2.46)) or (not(13.6 <= a <= 13.6)):
                self.log("Некорректные габариты.")
                return
        transport_types = ['Gazel', 'Bichok', 'MAN10', 'Fura']
        if choice not in [1, 2, 3, 4]:
            self.log("Некорректно выбран транспорт.")
            return
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO cars (type, a, b, c, weight)
        VALUES (?, ?, ?, ?, ?)
        ''', (transport_types[choice-1], a, b, c, tr))
        self.conn.commit()
    def del_transport(self):
        self.show_transport()
        choice = int(input("Выберите номер транспорта для удаления: "))
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM cars WHERE id = ?', (choice,))
        self.conn.commit()
    def show_transport(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT id, type, a, b, c, weight FROM cars 
        WHERE is_available = 1
        ''')
        cars = cursor.fetchall()
        if not cars:
            self.log("Нет доступного транспорта")
            return
        for car in cars:
            print(f"{car[0]}: {car[1]} ({car[2]}x{car[3]}x{car[4]}, грузоподъемность: {car[5]})")
    def applic(self):
        self.a, self.b, self.c, self.weight = map(int, input("Введите габариты (a * b * c) и вес: ").split())
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
            SELECT id, type, a, b, c, weight FROM cars 
            WHERE a >= ? AND b >= ? AND c >= ? AND weight >= ? AND is_available = 1
            LIMIT 1
            ''', (self.a, self.b, self.c, self.weight))
            car = cursor.fetchone()
            if car:
                car_id, car_type, a, b, c, weight = car
                cursor.execute('''
                INSERT INTO applications (car_id, a, b, c, weight)
                VALUES (?, ?, ?, ?, ?)
                ''', (car_id, self.a, self.b, self.c, self.weight))
                cursor.execute('UPDATE cars SET is_available = 0 WHERE id = ?', (car_id,))
                self.conn.commit()
                self.log(f"Заявка создана, машина {car_type} забронирована")
            else:
                self.log("Не нашлось подходящей машины.")
        except sqlite3.Error as e:
            self.error(f"Ошибка базы данных: {str(e)}")
            self.conn.rollback()
    def show_applications(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM applications")
            applications = cursor.fetchall()    
            if not applications:
                self.log("Нет активных заявок.")
                return
            for app in applications:
                app_id, car_id, a, b, c, weight = app
                cursor.execute("SELECT type, a, b, c, weight FROM cars WHERE id = ?", (car_id,))
                car = cursor.fetchone()
                if car:
                    car_type, car_a, car_b, car_c, car_weight = car
                    print(f"Заявка #{app_id}:")
                    print(f"  Машина: {car_type} ({car_a}x{car_b}x{car_c}, грузоподъёмность: {car_weight})")
                else:
                    print(f"Заявка #{app_id}: (машина удалена)")
                print(f"  Груз: {a}x{b}x{c}, вес: {weight}")
                print("-" * 30)
        except sqlite3.Error as e:
            self.error(f"Ошибка при получении заявок: {str(e)}")
    def remove_applic(self):
        self.show_applications()
        try:
            choice = int(input("Выберите номер заявки для удаления: "))
            cursor = self.conn.cursor()
            cursor.execute('SELECT car_id FROM applications WHERE id = ?', (choice,))
            application = cursor.fetchone()
            if not application:
                self.log("Заявка не найдена!")
                return
            car_id = application[0]
            cursor.execute('DELETE FROM applications WHERE id = ?', (choice,))
            cursor.execute('UPDATE cars SET is_available = 1 WHERE id = ?', (car_id,))
            self.conn.commit()
            self.log("Заявка удалена, машина возвращена в парк")
        except ValueError:
            self.log("Некорректный номер заявки")
        except sqlite3.Error as e:
            self.error(f"Ошибка базы данных: {str(e)}")
            self.conn.rollback()
    def exxit(self):
        self.conn.close()
        exit()
    def show_all_transport(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, type, a, b, c, weight, is_available FROM cars')
        cars = cursor.fetchall()
        for car in cars:
            status = "доступна" if car[6] else "занята"
            print(f"{car[0]}: {car[1]} ({car[2]}x{car[3]}x{car[4]}, грузоподъемность: {car[5]}, статус: {status})")
        
class TerminalError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Ошибка: '{value}' нельзя преобразовать в число.")

class TerminalGUI:
    def __init__(self, terminal):
        self.terminal = terminal
        self.root = Tk()
        self.root.title("ДЗ")
        self.root.geometry("800x600")
        self.setup_ui()
        self.root.mainloop()
    def setup_ui(self):
        menubar = Menu(self.root)
        transport_menu = Menu(menubar, tearoff=0)
        transport_menu.add_command(label="Показать транспорт", command=self.show_transport)
        transport_menu.add_command(label="Добавить транспорт", command=self.add_transport_dialog)
        transport_menu.add_command(label="Удалить транспорт", command=self.delete_transport_dialog)
        menubar.add_cascade(label="Транспорт", menu=transport_menu)
        applications_menu = Menu(menubar, tearoff=0)
        applications_menu.add_command(label="Показать заявки", command=self.show_applications)
        applications_menu.add_command(label="Создать заявку", command=self.create_application_dialog)
        applications_menu.add_command(label="Удалить заявку", command=self.delete_application_dialog)
        menubar.add_cascade(label="Заявки", menu=applications_menu)
        menubar.add_command(label="Выход", command=self.root.quit)
        self.root.config(menu=menubar)
        self.output_text = Text(self.root, wrap=WORD, state='disabled')
        self.output_text.pack(fill=BOTH, expand=True, padx=10, pady=10)
    def log(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(END, message + "\n")
        self.output_text.config(state='disabled')
        self.output_text.see(END)
    def show_transport(self):
        self.log("\n=== Доступный транспорт ===")
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.terminal.show_transport()
        sys.stdout = old_stdout
        self.log(mystdout.getvalue())
    def show_applications(self):
        self.log("\n=== Активные заявки ===")
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.terminal.show_applications()
        sys.stdout = old_stdout
        self.log(mystdout.getvalue())
    def add_transport_dialog(self):
        dialog = Toplevel(self.root)
        dialog.title("Добавить транспорт")
        Label(dialog, text="Тип транспорта:").grid(row=0, column=0, padx=5, pady=5)
        transport_type = ttk.Combobox(dialog, values=["Газель", "Бычок", "MAN10", "Фура"])
        transport_type.grid(row=0, column=1, padx=5, pady=5)
        Label(dialog, text="Габариты (a b c):").grid(row=1, column=0, padx=5, pady=5)
        dimensions_entry = Entry(dialog)
        dimensions_entry.grid(row=1, column=1, padx=5, pady=5)
        def add_transport():
            try:
                type_map = {"Газель": 1, "Бычок": 2, "MAN10": 3, "Фура": 4}
                choice = type_map[transport_type.get()]
                dimensions = dimensions_entry.get()
                with patch('sys.stdin', io.StringIO(f"{choice}\n{dimensions}\n")):
                    self.terminal.add_transport()
                self.log(f"Добавлен транспорт: {transport_type.get()}")
                dialog.destroy()
                self.show_transport()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        Button(dialog, text="Добавить", command=add_transport).grid(row=2, columnspan=2, pady=10)
    def delete_transport_dialog(self):
        self.show_transport()
        dialog = Toplevel(self.root)
        dialog.title("Удалить транспорт")
        Label(dialog, text="Введите ID транспорта для удаления:").pack(padx=10, pady=5)
        transport_id_entry = Entry(dialog)
        transport_id_entry.pack(padx=10, pady=5)
        def delete_transport():
            try:
                transport_id = transport_id_entry.get()
                with patch('sys.stdin', io.StringIO(f"{transport_id}\n")):
                    self.terminal.del_transport()
                self.log(f"Удален транспорт с ID: {transport_id}")
                dialog.destroy()
                self.show_transport()  
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        Button(dialog, text="Удалить", command=delete_transport).pack(pady=10)
    def create_application_dialog(self):
        dialog = Toplevel(self.root)
        dialog.title("Создать заявку")
        Label(dialog, text="Габариты груза и вес (a b c weight):").grid(row=0, column=0, padx=5, pady=5)
        cargo_entry = Entry(dialog)
        cargo_entry.grid(row=0, column=1, padx=5, pady=5)
        def create_application():
            try:
                cargo_data = cargo_entry.get()
                with patch('sys.stdin', io.StringIO(f"{cargo_data}\n")):
                    self.terminal.applic()
                self.log("Создана новая заявка")
                dialog.destroy()
                self.show_applications()
                self.show_transport()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        Button(dialog, text="Создать", command=create_application).grid(row=1, columnspan=2, pady=10)
    def delete_application_dialog(self):
        self.show_applications()
        dialog = Toplevel(self.root)
        dialog.title("Удалить заявку")
        Label(dialog, text="Введите ID заявки для удаления:").pack(padx=10, pady=5)
        app_id_entry = Entry(dialog)
        app_id_entry.pack(padx=10, pady=5)
        def delete_application():
            try:
                app_id = app_id_entry.get()
                with patch('sys.stdin', io.StringIO(f"{app_id}\n")):
                    self.terminal.remove_applic()
                self.log(f"Удалена заявка с ID: {app_id}")
                dialog.destroy()
                self.show_applications()
                self.show_transport()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
        Button(dialog, text="Удалить", command=delete_application).pack(pady=10)

A=Terminal()
TerminalGUI(A)