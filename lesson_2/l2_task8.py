"""Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры. """

cnt = 0


def func(set_of_numbers, specific_number):
    global cnt
    if set_of_numbers % 10 == specific_number:
        cnt += 1
    if set_of_numbers == 0:
        return cnt
    else:
        return func(set_of_numbers // 10, specific_number)


number_a = int(input("Введите последовательность чисел: "))
number_b = int(input("Введите цифру которую необходимо подсчитать: "))
answer = func(number_a, number_b)
print(answer)
