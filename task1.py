# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

from random import randint
  
def mas(n, m):
    return [[randint(2, 5) for _ in range(m)] for _ in range(n)]
  
def print_mas(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("{:3d}".format(a[i][j]), end="")
        print()
 
n = int(input("Введите количество групп: "))
m = int(input("Введите количество человек в группе (от 20 до 30): "))
a = mas(n, m)
print("Итоги экзамена:")
print_mas(a)

ski = []
for i in range (len(a)):
    stroki=0
    for j in range (len(a[0])):
        stroki+=a[i][j]
    ski.append(stroki)

max_element = 0
for i in range(len(ski)):
  if ski[i] > max_element:
    max_element = ski[i]
    ind = i

print(f"Наилучший средний балл равный {max_element} у группы номер {ind + 1}")