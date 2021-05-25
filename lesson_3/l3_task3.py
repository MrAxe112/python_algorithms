"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE, MIN_ELEM, MAX_ELEM = 10, -100, 100
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(array)

minimal_number, maximal_number = 0, 0

for i in range(len(array)):
    if array[i] < array[minimal_number]:
        minimal_number = i
    elif array[i] > array[maximal_number]:
        maximal_number = i

array[minimal_number], array[maximal_number] = array[maximal_number], array[minimal_number]
print(array)
