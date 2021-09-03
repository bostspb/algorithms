"""
Задача №3
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

x1, y1 = int(input('Enter x1\n')), int(input('Enter y1\n'))
x2, y2 = int(input('Enter x2\n')), int(input('Enter y2\n'))

# y = kx + b
k = (y2 - y1) / (x2 - x1)
b = - (x1 * y2 - x1 * y1) / (x2 - x1) + y1

print(f'y = {k}x + {b}')