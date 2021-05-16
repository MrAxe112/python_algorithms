"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5). """

user_number = int(input('Введите натуральное число: '))
last_input = user_number
even_numbers, odd_numbers = 0, 0


while user_number > 0:
    compared_number = user_number % 10
    if compared_number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    user_number //= 10


print(f'В числе {last_input} содержится {even_numbers} четных чисел и {odd_numbers} нечетных чисел')
