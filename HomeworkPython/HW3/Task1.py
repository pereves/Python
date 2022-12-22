# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной
# позиции.

from random import randint
def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list
n = int(input('Введите число N: '))
numbers = list(n)
print(f'Список {numbers}')
summ = 0
for i in range(1, len(numbers), 2):
    summ += numbers[i]
print(f"{numbers} -> сумма элементов на нечётных позициях: {summ}")