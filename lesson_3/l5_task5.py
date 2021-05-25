"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
минимальный и максимальный элементы в сумму не включать. """

import random

SIZE, MIN_ELEM, MAX_ELEM = 10, 1, 100
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(array)

minimal_number, maximal_number, result = 0, 0, 0

for i in range(1, len(array)):
    if array[i] < array[minimal_number]:
        minimal_number = i
    elif array[i] > array[maximal_number]:
        maximal_number = i

print(f'Минимальный элемент - {array[minimal_number]},\nМаксималный элемент - {array[maximal_number]}')

if minimal_number > maximal_number:
    minimal_number, maximal_number = maximal_number, minimal_number

for i in range(minimal_number + 1, maximal_number):
    result += array[i]

print(f'Сумма между элементами равна: {result}')
