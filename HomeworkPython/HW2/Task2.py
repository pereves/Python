# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input ('Введите N: '))
composition = 1
for i in range (N):
    i += 1
    composition *= i
    print(composition, end=' ')

