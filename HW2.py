
# HW

# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

health = int(input('Enter health value: '))
if health <= 0:
    print('False')
else:
    print('True')

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”, а иначе - “Нечетное”

n = int(input('Enter the number: '))
if n % 2 == 0:
    print('четное')
else:
    print('нечетное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
# которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако,
# если год делится без остатка  на 400, он также считается високосным (1200, 2000)

year = int(input('Enter year: '))
if year % 4 == 0 and year % 10 % 10 != 0:
    print('Високосный')
elif year % 400 == 0 and year != 400:
    print('Високосный')
else:
    print('Год обычный')


# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

text = input('Enter text: ')
n = int(input('How much times you want to print the text?: '))
for i in range(1, n + 1):
    print(text)
    i += 1

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
operation = input('Введите операцию (+, -, /, *): ')
if operation == '+':
    print(f'{num1}{operation}{num2} = {num1 + num2}')
elif operation == '-':
    print(f'{num1}{operation}{num2} = {num1 - num2}')
elif operation == '/':
    print(f'{num1}{operation}{num2} = {num1 / num2}')
elif operation == '*':
    print(f'{num1}{operation}{num2} = {num1 * num2}')
else:
    print(f'Введите корректный оператор')

