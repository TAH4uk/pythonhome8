# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import numpy

r = int(input("Введите размер квадратной матрицы: "))

matr = numpy.matrix(numpy.random.randint(10, size = (r, r)))
print()
print("Полученная матрица: ")
print(matr)

sumstr = matr.sum(axis = 1)
print()
print("Суммы всех строк матрицы: ")
print(sumstr)

diag = numpy.diagonal(matr)
print()
print("Главная диагнональ матрицы: ")
print(diag)

sumdiag = sum(diag)
print()
print("Суммы главной диагнонали матрицы: ")
print(sumdiag)

print()
count = 1
for i in sumstr:
    if i[0] > sumdiag:
        print(f"Сумма строки {count} равная {i[0]} больше суммы главной диагонали матрицы равной {sumdiag}")
        count += 1
    else:
        print(f"Сумма строки {count} равная {i[0]} меньше суммы главной диагонали матрицы равной {sumdiag}")
        count += 1