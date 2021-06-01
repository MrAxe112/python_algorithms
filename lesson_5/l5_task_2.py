"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’,
‘C’, ‘9’, ‘F’, ‘E’]. """
import collections
from string import hexdigits


def hex_int(string):
    hx = 0
    string.reverse()
    for i in range(len(string)):
        hx += hex_dct[string[i]] * 16 ** i
    return hx


def int_hex(number):
    num = collections.deque()
    while number > 0:
        rem = number % 16
        for i in hex_dct:
            if hex_dct[i] == rem:
                num.append(i)
        number //= 16
    num.reverse()
    return list(num)


hex_dct = collections.defaultdict(int)
hex_nums = hexdigits[:-6].upper()
counter = 0
for key in hex_nums:
    hex_dct[key] += counter
    counter += 1

a = collections.deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
b = collections.deque(input('Введите второе число в hex формате (только цифры от 0 до f): ').upper())

num_a, num_b = hex_int(a), hex_int(b)

print(f'Сумма чисел  =  {int_hex(num_a + num_b)}')
print(f'Произведение чисел  = {int_hex(num_a * num_b)}')
