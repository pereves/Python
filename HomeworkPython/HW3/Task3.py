# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.(если получаются длинные числа после запятой, это нормально и особенность данного
# языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))

n = [1.1, 1.2, 3.1, 10.01]
max = 0
min = 1
for i in n:
    temp = round(i %1, 3)
    print(temp)
    if temp > max:
        max = temp
    elif temp < min:
        min = temp
print(f"max {max} min {min}")
print(f"{max - min}")
