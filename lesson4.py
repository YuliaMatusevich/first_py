# min_item = min(1, 2, 8)
# print(min_item)
#
# def person(age, first_name, last_name):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} y.o..'
#
# print(person(28, 'Ivanova', 'Maria'))
#
# def person1(age, first_name ='Anna', last_name = 'Ivanova'):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} y.o..'
#
# print(person1(first_name='Anna', age = 28, last_name ='Ivanova' ))
# print(person1(25))
#
# def pattern(length, char1='/', char2='*'):
#     return (char1+char2) * length +char1
#
# print(pattern(9))
# print(pattern(9, char1='++'))
# print(pattern( char2='>>', length=8))
#
# def decorator_func(func):
#     def wrapper(*args):
#         print('Wrapper fucntion')
#         print(f'Calling function {func.__name__}')
#         print((f'With arguments: {args}'))
#         print('Wrapper function in progress')
#         print(func(*args))
#         print('Exiting wrapper')
#     return wrapper
#
# @decorator_func
# def hello(item):
#     return f'{item} is wrapped'
#
# hello('Candy')
#

# x = 15
# y  = 20
# def sum(x,y):
#     print(f'locals: {locals()}')
#     return x + y
#
# print(f'Inside function: {sum(8,15)}')
# print(f'Outside function: {x + y}')
# print(f'Globals: {globals()}')

# name = 'Anna'
# def outer_function():
#     name='Elena'
#     def inner_function():
#         #name='John'
#         return name
#     print(name)
#     return inner_function
#     return name
#
# # closure = outer_function()
# # result = closure()
# # print(result)
#
# print(outer_function())
# outer_function()


# result = lambda n: n * n
# print(result(5))
#

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 100]
# def filterAndSum(lst):
#     new_l = []
#     for x in lst:
#         if isinstance(x, int):
#             new_l.append(x)
#     return sum(new_l)
#
# print(filterAndSum(list_1))
#
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
# print(filtered)
#
#
#
# from functools import reduce
#
# result = reduce(lambda x, y: x * y, [1, 3, 6, 7]) #будет исполнять по нарастанию. типа сначала 1 * 3, потом x стало 3, а у = 6, потом х  = 3*6 = 18, а у = 7
# print(result)

result = list(map(lambda x: x**2, [1, 3, 6, 7]))
print(result)

from math import prod

l =[1, 3, 6, 7]
print(prod(l))

import math #as m можно использовать alias для названий модуля.
#from math import *
l = [2, 4, 6, 8]
print(math.prod(l))

from my_module import *
print(sum_it(2, 8))


def tests():
    assert sum_it(5, 8) == 13, 'ERROR'
    #assert sum_it(5, 8) == 10, 'ERROR'

tests()

import datetime
birthYear = 1984
current_date = datetime.date.today()
print(current_date)

current_age = current_date.year - birthYear
print(current_age)

lst = [8, 3, 5, 9, -2]
lst.sort()
print(lst)
print(sorted(lst))

#sort - с листами(меняет начальные лист), sorted - с любыми объектами(создает новый объект)

tup = { 5, 8, 7, 1, 0, 0}
print(sorted(tup))

dct = {1: 'q', 2: 'w', 3: 'e'}
for key in dct:
    print(dct[key])

for value in dct.values():
    print(value)

for key, value in dct.items():
    print(f'{key} {value}')


a = dct.get(1) #q
#a = dct.get(10) #None
print(a)

b = dct.setdefault(4, 'r')
print(b)
print(dct)
