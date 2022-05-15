import tkinter as tk  # подключаем  tkinter

# Подключаем  модуль с диалоговыми  окнами  tkinter:
from tkinter.messagebox import *

root = tk.Tk()  # создаем главное окно

# Устанавливаем минимальные и максимальные размеры окна:
root.minsize(width=350, height=150)
root.maxsize(width=800, height=500)

root.title("Калькулятор")  # заголовок окна

#  Создадим 3 фрейма:   	fr_xy,        fr_op    и     fr_res
#  для размещения компонент.

# фрейм fr_xy – компоненты для ввода чисел x, y:
fr_xy = tk.Frame(root, bg='white', cursor='shuttle')
fr_xy.pack(side='top', expand=YES, fill='both')

# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = tk.Label(fr_xy, text="x = ")
pack = lx.pack(side='left', padx=10, pady=10)
entX = tk.Entry(fr_xy)
entX.insert(0, 0)  # – в редактор записываем в позицию 0 число 0
entX.pack(side='left', padx=10, pady=10)
# Редактор будет выбран при старте (иметь фокус ввода):
entX.focus()
ly = tk.Label(fr_xy, text="y = ")
ly.pack(side='left', padx=10, pady=10)

entY = tk.Entry(fr_xy)
entY.insert(0, 0)
entY.pack(side='left', padx=10, pady=10)

# Создание фрейма с заголовком fr_op  – выбор операции:
fr_op = tk.LabelFrame(root, text="Операция:", bg='blue', cursor='plus')
fr_op.pack(side='top', expand=YES, fill='both')

#  Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['+', '-', '*', '/']  # –  список операций
#   Вводим строковую переменную tkinter, ее свяжем с выбором
#   Radiobutton
varOper = tk.StringVar()
#  В цикле создаем 4 кнопки Radiobutton (связываем их
# с созданной переменной varOper):
for op in oper:
    tk.Radiobutton(fr_op, text=op, variable=varOper,
                   value=op).pack(side='left',
                                  padx=20, pady=10)

# Устанавливаем текущее значение ‘+’:
varOper.set(oper[0])
#  Создаем 3-й фрейм fr_res – вычисление значения
#  и вывод результата:
fr_res = tk.Frame(root, bg='red', cursor='heart')
fr_res.pack(side='top', expand=YES, fill='both')


# Обработчик кнопки:
def OnButtunResult():
    #  Защищенный блок, будем пытаться перевести текст
    #  из редактора Entry в число:
    try:
        x = float(entX.get())  # извлекаем число из 1-го редактора
    except ValueError:
        # если не получилось, выдаем сообщение и выходим:
        showerror("Ошибка заполнения",
                  "Переменная x не является числом")
        return
    # Защищенный блок 2:
    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения",
                  "Переменная y не является числом")
        return
    #  В переменную op записываем выбранную операцию:
    op = varOper.get()
    #  Вычисляем:
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        if y != 0:
            res = x / y
        else:
            res = 'NAN'
    else:
        res = 'операция выбрана неправильно'
    # Вывод результата на метку:
    lres['text'] = res


# Обработчик кнопки закончился.

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
tk.Button(fr_res, text="=", width=10,
          command=OnButtunResult).pack(side='left',
                                       padx=30, pady=20)
lres = tk.Label(fr_res, text="")
lres.pack(side='left', padx=30, pady=20)

# Запуск цикла обработки сообщений:
root.mainloop()
