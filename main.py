import tkinter as tk

win = tk.Tk() # создание окна
win.geometry(f"240x260+100+200") # задание размерав окна и координаты появления окна на экране
win.resizable(False, False)# задание условия изменения размера окна(False False) изменить размер нельзя,
                           # (False True) изменение только по координатам Y (ВЕРТИКАЛЬ)
                           # (True False) изменение только по координатам X (ГОРИЗОНТАЛЬ)
                           # (True True) изменения по X и Y координатам
win.minsize(100, 100)# задание минимального размера окна
win.maxsize(500, 500)# задание максимального  размера окна
win['bg'] = '#33ffe6' # задание цвета окна
win.title('КАЛЬКУЛЯТОР')# задание названия окна

#photo = tk.PhotoImage(file='путь к файлу с изображением')
#win.iconphoto(False, photo) # создание иконки в окне.

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15) # Entry создание поля ввода информации в окне
calc.insert(0, 0)
calc.grid(row=2, column=0, columnspan=4, stick='we', padx = 5) # grid метод для расположения виджита в окне в виде таблицы

def add_digit(digit): # функция вывода числа при нажатии на кнопку в поле ввода информации
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(2, value + digit)

def add_operation(operation): # функция вывода числа при нажатии на кнопку в поле ввода информации
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(2, value + operation)

def add_claner(): # функция очищения поле ввода информации
    calc.delete(0,tk.END)
    calc.insert(0, 0)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda : add_digit(digit))

def make_digit_button_a(C):
    return tk.Button(text='C', bd=5, font=('Arial', 13), command=lambda : add_claner())

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg = 'red',  command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg = 'red',  command=lambda : add_digit(operation))


make_digit_button('1').grid(row=3, column=0, stick='wens', padx=5, pady=5)# Button создание кнопки
make_digit_button('2').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=5, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=6, column=0, stick='wens', padx=5, pady=5)
make_digit_button_a('C').grid(row=6, column=1, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=5, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=6, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=6, column=2, stick='wens', padx=5, pady=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)


win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)
win.grid_rowconfigure(6, minsize=60)




win.mainloop()












