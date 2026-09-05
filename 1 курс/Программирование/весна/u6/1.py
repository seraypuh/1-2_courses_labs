from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(arg1.get())
        num2 = float(arg2.get())
        res = []
        canvas.delete("all")
        if choice.get() == 1:
            if sum_var.get():
                res.append(f"Сумма: {round(num1 + num2, 2)}")
            if sub_var.get():
                res.append(f"Разность: {round(num1 - num2, 2)}")
            if mul_var.get():
                res.append(f"Произведение: {round(num1 * num2, 2)}")
            if div_var.get():
                if num2 != 0:
                    res.append(f"Частное: {round(num1 / num2, 2)}")
                else:
                    res.append("Деление на 0!")
            if res:
                result_label.config(text="\n".join(res))
            else:
                result_label.config(text="Выбери хотя бы одну операцию!")
        else:
            if area.get():
                if num1 > 0 and num2 > 0:
                    res.append(f"Площадь: {round(num1 * num2, 2)}")
                else:
                    res.append("Неверные значения!")
            if perimeter.get():
                if num1 > 0 and num2 > 0:
                    res.append(f"Периметр: {round(2 * (num1 + num2), 2)}")
                else:
                    res.append("Неверные значения!")
            if res:
                result_label.config(text="\n".join(res))
            else:
                result_label.config(text="Выбери хотя бы одну операцию!")
            w = num1
            h = num2
            if w>0 and h>0:
                x0 = 10
                y0 = 10
                x1 = x0 + w
                y1 = y0 + h
                canvas.create_rectangle(x0, y0, x1, y1, fill="lightgreen", outline="black")
        
    except:
        result_label.config(text="Некорректный ввод!")
        canvas.delete("all")

def switch_mode():
    sum_var.set(0)
    sub_var.set(0)
    mul_var.set(0)
    div_var.set(0)
    area.set(0)
    perimeter.set(0)
    if choice.get() == 1:
        areaa.grid_forget()
        perimeterr.grid_forget()
        summ.grid(row=1, column=2, sticky="", padx=5)
        subb.grid(row=1, column=3, sticky="", padx=5)
        mull.grid(row=2, column=2, sticky="", padx=5)
        divv.grid(row=2, column=3, sticky="", padx=5)
    else:
        summ.grid_forget()
        subb.grid_forget()
        mull.grid_forget()
        divv.grid_forget()
        areaa.grid(row = 1, column=2, sticky="", padx=5)
        perimeterr.grid(row = 1, column=3, sticky="", padx=5)
    update_opreations()

def showpopup():
    messagebox.showinfo("Справка", "Сделал Пухарев Сергей 23.04.2025")

def clear_entries():
    arg1.delete(0, END)
    arg2.delete(0, END)
    result_label.config(text="") 

def enable_sum(): sum_var.set(1)
def enable_sub(): sub_var.set(1)
def enable_mul(): mul_var.set(1)
def enable_div(): div_var.set(1)
def enable_area(): area.set(1)
def enable_perimeter(): perimeter.set(1)

def update_opreations():
    operations.delete(0, END)

    if choice.get() == 1:
        operations.add_command(label="Сложение", command=enable_sum)
        operations.add_command(label="Вычитание", command=enable_sub)
        operations.add_command(label="Умножение", command=enable_mul)
        operations.add_command(label="Деление", command=enable_div)
    else:
        operations.add_command(label="Площадь", command=enable_area)
        operations.add_command(label="Периметр", command=enable_perimeter)

    operations.add_separator()
    operations.add_command(label="Очистить данные", command=clear_entries)


tk = Tk()
tk.title("Задание")
tk.geometry("1280x720")
tk.minsize(700, 300)

menu_bar = Menu(tk)
file = Menu(menu_bar, tearoff=0)
file.add_command(label="Выход", command=tk.quit)
menu_bar.add_cascade(label="Файл", menu=file)
operations = Menu(menu_bar, tearoff=0)
operations.add_command(label="Очистить данные", command=clear_entries)
menu_bar.add_cascade(label="Операции", menu=operations)
info = Menu(menu_bar, tearoff = 0)
info.add_command(label="Кто сделал?", command=showpopup)
menu_bar.add_cascade(label="Справка", menu=info)

choice = IntVar(value=1)
rb1 = Radiobutton(tk, text="Калькулятор", variable=choice, value=1, command=switch_mode)
rb1.grid(row=5, column=0, padx=5, pady=10)
rb2 = Radiobutton(tk, text="Прямоугольник", variable=choice, value=2, command=switch_mode)
rb2.grid(row=5, column=1, padx=5, pady=10)

text1 = Label(text="Значение 1")
text2 = Label(text="Значение 2")
arg1 = Entry(tk, width = 30)
arg2 = Entry(tk, width = 30)
text1.grid(row=0, column=0, padx = 5, pady=10)
text2.grid(row=0, column=1, padx = 5, pady=10)
arg1.grid(row=1, column=0, padx = 5, pady=10)
arg2.grid(row=1, column=1, padx = 5, pady=10)

sum_var = IntVar()
sub_var = IntVar()
mul_var = IntVar()
div_var = IntVar()

summ = Checkbutton(tk, text="+", variable=sum_var)
subb = Checkbutton(tk, text="-", variable=sub_var)
mull = Checkbutton(tk, text="*", variable=mul_var)
divv = Checkbutton(tk, text="/", variable=div_var)

area = IntVar()
perimeter = IntVar()

areaa = Checkbutton(tk, text="Площадь", variable=area)
perimeterr = Checkbutton(tk, text="Периметр", variable=perimeter)

ttk.Button(tk, text="Вычислить", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)
result_label = Label(tk, text="", fg="green", justify="center")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

canvas = Canvas(tk, width=10000, height=10000, bg="white", bd=5, relief=GROOVE)
canvas.grid(row=10, column=10, rowspan=6, columnspan=2, padx=20, pady=10)

tk.config(menu=menu_bar)
switch_mode()
tk.mainloop()