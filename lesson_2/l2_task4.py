"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843"""


def func(number, res=0):
    if number == 0:
        return res
    else:
        return func(number // 10, res * 10 + number % 10)


user_number = input("Введите число, которое будет обрашено в обатный порядок: ")
result = func(int(user_number))
print(result)
