# 1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3
# значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
def quad(x):
    per = x * 4
    sq = x * x
    diag = (x * x + x * x) ** 0.5
    return per, sq, diag
a = 4
print(quad(a))

# 2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def my_f(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

my_f(name="John", last_name="Smith", age=35, position="web developer")


# 3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только положительные числа

mult = lambda x, y, z: x * y * z
print(mult(5, 8, 2))

my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
print(filtered)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce
result = reduce(lambda x, y: x * y, new_list)
print(result)


# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он
# принимает в качестве параметра

import time
def timing_decorator(func):
    def timeT(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        ex_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {ex_time:.20f} секунд")
        return result
    return timeT
@timing_decorator
def quad(x):
    per = x * 4
    sq = x * x
    diag = (x * x + x * x) ** 0.5
    return per, sq, diag

a = 1234567888887868668
print(quad(a))


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

from my_calc import *

print(plus(4, 5))
print(minus(4, 5))
print(multiply(4, 5))
print(divide(4, 5))
print(power(4, 5))