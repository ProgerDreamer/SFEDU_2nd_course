from tkinter import *

from tkinter.messagebox import *

root = Tk()

root.title("Главное окно программы")

root.geometry("300x100+500+280")

label1 = Label(root, bg='#555555')

label1.pack(anchor="center", expand=YES, fill=X)


def close_query():
    showwarning('Предупреждение', 'Внимание! Что-то пошло не так.')
    root.destroy()


Button(label1, text='Выход', command=close_query).pack(side=RIGHT, padx=120, pady=5)

root.mainloop()
