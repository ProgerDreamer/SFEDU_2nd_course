# Создать файл, содержащий целые числа.
# В файле создается случайное ко-личество  строк (от 1  до 5),
# в каждой  строке случайное количество  целых чисел (от 0 до 5).
# Числа в каждой строке, разделены пробелами.


from random import randint
import os

text1 = open('text.txt', 'w')
row = randint(1, 5)

for i in range(row):
    col = randint(0, 5)
    for j in range(col):
        x = randint(-100, 100)
        text1.write(str(x) + ' ')
    text1.write('\n')

text1.close()
