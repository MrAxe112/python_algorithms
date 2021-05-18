"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и какие между ними растояние.
"""
print('Введите две буквы. Будет вычеслено на каких позициях алфавита стоят буквы и растояние между этими буквами')

first_letter = input('1-я буква: ')
second_letter = input('2-я буква: ')

f_letter, s_letter = first_letter, second_letter

first_letter = ord(first_letter) - ord('a') + 1
second_letter = ord(second_letter) - ord('a') + 1

print(f'Позиция буквы "{f_letter}" это {first_letter} и позиция буквы "{s_letter}" это {second_letter}.')

if first_letter == second_letter:
    print("Так как обе буквы одинаковы, растояния между ними нет")
else:
    print(f'Между буквами {abs(first_letter - second_letter) - 1} символов.')
