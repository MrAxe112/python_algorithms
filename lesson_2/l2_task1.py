"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в
качестве делителя. """

while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input("Введите символ операции '+', '-', '*', '/'. Для выхода из программы '0': ")
    if c == "+":
        print(f'Ответ: {a + b}')
    elif c == "-":
        print(f'Ответ: {a - b}')
    elif c == "*":
        print(f'Ответ: {a * b}')
    elif c == "/":
        if b == 0:
            print('Делить на ноль нельзя')
        else:
            print(f'Ответ: {a / b}')
    elif c == "0":
        print("Завершение программы")
        break
    else:
        print("Ошибка, принимаются только '+', '-', '*', '/'. Для выхода из программы'0':")
