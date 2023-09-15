import math
from functools import reduce
from my_calc import *
from time import *

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
def square(side):
    p = side * 4
    s = side * side
    d = round(side * (math.sqrt(2)), 2)
    return p, s, d

print(square(5))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#     в формате аргумент: значение. Например:
	# name: John
	# last_name: Smith
	# age: 35
	# position: web developer

def person (**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

person(name = 'Anna', age = 32)

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x >= 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
print(reduce(lambda x, y: x * y, my_list))


# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
def decorator(function):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        function(*args, **kwargs)
        end = perf_counter_ns()
        print(f'Время выполнения функции: {end - start} наносекунд')
    return wrapper

list_1 = [12, -8, 5, 11, 14]

@decorator
def odd_numbers(lst):
    print(list(filter(lambda x: x % 2 == 1, lst)))

odd_numbers(list_1)


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

print(sum_num(-9, 12))
print(dif_num(12,154))
print(prod_num(2,12))
print(quot_num(4,-1))

