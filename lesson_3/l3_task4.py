"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE, MIN_ELEM, MAX_ELEM = 1000, -1000, 1000
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(array)

num = array[0]
max_frq = 1
for i in range(len(array) - 1):
    frq = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f"Число {num} встречается {max_frq} раз")
else:
    print("Все элементы уникальны")
