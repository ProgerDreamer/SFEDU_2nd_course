import tkinter as tk
from tkinter.messagebox import *

from Condition_with_shell import Condition


def conditional_max(li, condition_obj):
    out = condition_obj.no_true_value
    for elem in li:
        if condition_obj.check(elem):
            if (elem > out) or (not condition_obj.check(out)):
                out = elem
    if condition_obj.check(out):
        return out
    else:
        return 'maximum not found'


root = tk.Tk()
root.minsize(width=500, height=300)
root.maxsize(width=900, height=600)

frame_enter = tk.Frame(root, bg='green')
frame_enter.pack(side='top', expand=tk.YES, fill='both')
top_label = tk.Label(frame_enter, text='Enter array elements\nusing a separator " "', bg='green', font=('times', 10, 'bold'))
top_label.pack(side='left', padx=10, pady=10)
entArray = tk.Entry(frame_enter, width=50)
entArray.pack(side='left', padx=10, pady=10, expand=tk.YES)
entArray.focus()

frame_result = tk.Frame(root, bg='yellow')
frame_result.pack(side='top', expand=tk.YES, fill='both')
lres = tk.Label(frame_result, text='')

condition_positive = Condition(lambda x: x > 0, -1)


def on_button_result():
    arr = entArray.get().split()
    try:
        for i, elem in enumerate(arr):
            arr[i] = int(elem)
    except ValueError:
        lres['text'] = 'Only integer elements allowed'
        return
    lres['text'] = conditional_max(arr, condition_positive)


button_res = tk.Button(frame_result, text='Max in positive: ', width=30, command=on_button_result)
button_res.pack(side='left', padx=10, pady=10)
lres.pack(side='left', padx=10, pady=10)

root.mainloop()
