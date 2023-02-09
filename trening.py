import tkinter as tk

def element(lista):
    lista2 = []
    lista1 = []

    for i in lista:
        if i < 0:
            lista2.append(i)
        else:
            lista1.append(i)

    lista1.sort()
    lista2.sort()
    if len(lista1) > len(lista2):
        for ell in lista2:
            for el2 in lista1:
                if el2 + ell == 0:
                    lista1.remove(el2)
        lista = lista1
        return lista
        print(lista)


    elif len(lista1) < len(lista2):
        for el2 in lista1:
            for ell in lista2:
                if el2 + ell == 0:
                    lista2.remove(ell)
        lista = lista2
        return lista
        print(lista)

    else:
        print('Все элементы парные')
lista = [-1, 1, 4, -4, -3, -2, -5, 5, -6, 6, 7, 3, -7, 2]
print(element(lista))

# def enter():
#     global variable
#     variable = 1
#     return variable
#
# def get_entry():
#
#     value = name.get()
#     if value:
#         print(value)
#     else:
#         print('ПУСТО')
# def delete_entry():
#     name.delete(0, tk.END)
#
#
# win = tk.Tk()
# win.geometry(f"400x500+150+200")
# win.title('Графическое приложение')
#
# tk.Label(win, text='ИМЯ').grid(row=0,column=0, stick='w')
#
# name = tk.Entry(win)
# name.grid(row=0,column=1)
#
# tk.Button(win, text='ДЕЙСТВИЕ', command=get_entry).grid(row=0, column=2)
# tk.Button(win, text='УДАЛЕНИЕ', command=delete_entry).grid(row=0, column=3)
# tk.Button(win, text='ВВОД', command=lambda: name.insert(1, variable)).grid(row=0, column=4)
# tk.Button(win, text='1', command=enter).grid(row=0, column=5)
# win.grid_columnconfigure(0, minsize=100)
# win.grid_columnconfigure(0, minsize=100)
#
# win.mainloop()