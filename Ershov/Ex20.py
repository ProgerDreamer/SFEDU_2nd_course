import os  # Для создание паузы перед закрытием консоли


# Функция проверки на простоту числа
def simplicity(n):
    if n != 1 and n != 2:
        d = 2
        flag = True
        while n >= d*d and flag:
            flag = n % d != 0
            d += 1
        return flag
    else:
        return False


# Создает фаил с простыми числами в диапозоне [start, end]
def create_file_with_simplicity_numbers(name, start, end):
    with open(name, "wb+") as f:
        # В цикле проверяю число на простоту, и если оно простое, то бобавляю в фаил
        for i in range(start, end + 1):
            if simplicity(i):
                bx = i.to_bytes(2, byteorder='little', signed=True)  # Перевод в bytes из int
                f.write(bx)  # Запись в фаил
    
        f.seek(0)  # В начало файла

        # Вывожу сам фаил для проверки 
        bx = f.read(2) 
        # Проверка на пустую строку bytes b'':
        while bx != b'': 
            # Перевод из bytes в число int:
            x = int.from_bytes(bx, byteorder='little', signed=True)
            # выводим числа на экран:
            print(x)
            # читаем из файла по 2 байта:
            bx = f.read(2)


# Создает фаил с простыми числами в диапозоне [100, 200]
create_file_with_simplicity_numbers("numbers.dat", 100, 200)

os.system("pause")  # Делаю остановку консоли
