"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8,
3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа. """

import random

SIZE, MIN_ELEM, MAX_ELEM = 100, -99, -9
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(array)

array_result = []

for a, b in enumerate(array):
    if b % 2 == 0:
        array_result.append(a)

print(array_result)
