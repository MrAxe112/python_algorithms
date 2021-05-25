"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

range_min, range_max, search_min, search_max = 2, 99, 2, 10

array_a = [i for i in range(range_min, range_max+1)]
array_b = [i for i in range(search_min, search_max)]
answer_list = [0]*len(array_b)

for num in array_a:
    for num_b in array_b:
        if num % num_b == 0:
            answer_list[num_b-2] += 1

for i, n in enumerate(answer_list):
    print(f"для числа {array_b[i]} - {n}")
