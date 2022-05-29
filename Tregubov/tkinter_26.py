# подключаем графический интерфейс
from tkinter import *

# подключаем диалоговые окна:
from tkinter.messagebox import *

# подключаем диалоговое окно выбор цвета
from tkinter.colorchooser import askcolor

# подключаем библиотеку для получения случайных чисел
from random import randint


# диалоговое окно выбор цвета
def color_ris():
    global res
    # вызываем окно
    res = askcolor()

    if res[1]:
        scele_w()


# закрытие приложения
def closeQuery():
    #  При нажатии на кнопку запускаем диалоговое окно.
    #  Спрашиваем у пользователя, закрывать ли программу:
    if askyesno('Выход из программы...', 'Закрыть программу? '):
        # Уничтожаем главное окно и поэтому закрываем программу:
        root.destroy()


# Создаем виджет ширины линии
def scele_w():
    global widget
    global ck
    # создаю новое окно
    ck = Toplevel(root)
    # удаляю кнопку развернуть и фиксирую размер виджета
    ck.resizable(0, 0)

    # добавляю виджет, лейбел и кнопку
    widget = Scale(ck, orient="vertical", resolution=1, from_=1, to=50)
    label_1 = Label(ck, text="Ширина")
    label_1.grid(row=0, column=0)
    widget.grid(row=0, column=1)
    button = Button(ck, text="Рисовать", command=ris)
    button.grid(row=1, column=1)


# обработка значений и рисование
def ris():
    global res
    global widget
    global ck

    # получаю все значения и обрабатываю
    w = widget.get()
    if res[1] and w:
        # проверяю размер окна, чтобы линия попала в окно даже при изменении размера
        s = root.geometry()
        s = s.split('+')
        s = s[0].split('x')
        width_root = int(s[0])
        height_root = int(s[1])
        # рисую линию с рандомными координатами и заданным цветом
        can.create_line(randint(0, width_root), randint(0, height_root), randint(0, width_root),
                        randint(0, height_root), fill=res[1], width=w)
        ck.destroy()


# создаю начальное окно
root = Tk()
root.title("Виджет Canvas, рисование ")
root.geometry("400x400+250+250")
root.minsize(width=350, height=150)

# создаем фрейм для размещения на нем кнопок:
win = Frame(root, bg='#555555', relief=RAISED)
win.pack(anchor="n", expand=YES, fill=X)

#  создаем область рисования Canvas:
can = Canvas(root)
can.pack(expand=YES, fill=BOTH)

# Создаем кнопки:
button2 = Button(win, text='Выход', width=10, height=1, command=closeQuery)
button2.pack(side='right', pady=(5, 5), padx=(5, 5))
button1 = Button(win, text='Цвет', width=10, height=1, command=color_ris)
button1.pack(side='right', pady=(5, 5), padx=(5, 5))

root.mainloop()
