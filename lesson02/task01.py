"""
Задача №1
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    operation = input('Enter operation sign or "0" for exit\n')
    if operation == '0':
        break
    elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('Incorrect operation sign, please, repeat')
    else:
        first_number = int(input('Enter first number\n'))
        second_number = int(input('Enter second number\n'))
        if operation == '+':
            print(f'{first_number} + {second_number} = {first_number + second_number}')
        elif operation == '-':
            print(f'{first_number} - {second_number} = {first_number - second_number}')
        elif operation == '*':
            print(f'{first_number} * {second_number} = {first_number * second_number}')
        elif operation == '/':
            if second_number == 0:
                print('Error: division on zero')
            else:
                print(f'{first_number} / {second_number} = {first_number / second_number}')


print('Program was stopped')
