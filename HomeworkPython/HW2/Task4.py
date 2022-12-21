# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в отдельном списке

from random import randint
def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list
n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))
for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)