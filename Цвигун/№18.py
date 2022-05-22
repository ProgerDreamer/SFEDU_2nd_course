import os


# удаление файла
os.remove(r'text.txt')

# проверка существования файла
if os.path.exists('text.txt'):
    print("файл существует")
else:
    print("файл не существует")
