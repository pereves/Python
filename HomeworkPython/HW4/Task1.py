# Вычислить число c заданной точностью d

x = float(input("Введите число:\n"))
d = int(input("Введите число для задания точности числа:\n"))
template = '{:.' + str(d) + 'f}'
print(f'Число {x} с заданной точностью {d} равно {template.format(x)}')