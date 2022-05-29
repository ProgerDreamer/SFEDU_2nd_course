from sympy import *
import matplotlib.pyplot as plt
import numpy as np


# 1.1
print('Задание №1.1')
x = Symbol('x')
L = limit(sin(x) / x, x, 0)
print('предел L =', L)
print()

# 2.2
print('Задание №2.2')
n = int(input('Введите натуральное число: '))
Rsum = 0.0
i = 1
while i <= n:
    s = 1.0 / (i ** 2)
    Rsum = Rsum + s
    i = i + 1
print('сумма ряда Rsum =', Rsum)
print()

# 3.1
print('Задание №3.1')
x = Symbol('x')
f = diff(sin(2 * x), x)
print('производная f =', f)
print()

# 4.1
print('Задание №4.1')
p = int(input('Введите натуральное число: '))
In = integrate(x ** p, x)
print(In)
print()

# 5.3
print('Задание №5.3')
r = np.roots([1, -1, -22, 40])
print(r)
print()

# 6.2
print('Задание №6.2')
fig, ax = plt.subplots()
x = np.linspace(-5, 5, 100)
y = x ** 3 - x ** 2 - 22 * x + 40
ax.plot(x, y)
plt.show()
