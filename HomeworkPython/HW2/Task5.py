# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random
N = int(input("Введите размер списка: "))
spam = list(range(1, N+1))
print("Начальный список : " + str(spam))
for i in range(len(spam) - 1, 0, -1):
    j = random.randint(0, i + 1)
    spam[i], spam[j] = spam[j], spam[i]
print("Перемешанный список : " + str(spam))