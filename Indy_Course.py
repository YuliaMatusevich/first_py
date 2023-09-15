# a, b = input("Enter two numbers: ").split() # вводится ТОЛЬКО 2 числа через пробел
# a = int(a)
# b = int(b)
# print(a, b)
# print(type(a),type(b))
#
#
# a, b, c = map(int, input("Enter 3 numbers: ").split()) #считываем 3 целых числа через пробел
# print(a,b,c)
from math import ceil

# age = int(input("Введите ваш возраст: "))
# print(age + 1)

#
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep=' ')
# print(1, 2, 3, 4, sep='')
# print(1, 2, 3, 4, sep=',')
# print(1, 2, 3, 4, sep='*')
# print(1, 2, 3, 4, sep='###')

# Если вы хотите добавить дополнительный перенос строки или отменить его вовсе, заменив любым символов,
# просто присвойте end новое значение в виде строки.

# print(1, 2, 3, end='!') #не будет переноса в конце
# print('hello') # здесь будет перенос
# print(5, 6, 7) # и здесь будет перенос
#
# # Можно одновременно пользоваться атрибутами sep и end . Задавать им значения можно в любом порядке, главное прописать имя атрибута
#
# print(1, 2, 3, sep='!', end='?')
# print('new', 'string')
# print(5, 6, 7, 8, 9, end='END', sep='@') # и здесь будет перенос
# print()
#
# print("Книга 'Война и мир' была написана в 1867 году")

# a = 1.999999999999999
# b = int(a)
# print(b)

# a = int(input())
# h = (a - a // 3600) // 60
# m = a % 60
# print(h, m)
#
# i = int(input())
# a = bool(i >= 0)
# print(a)

# i = int(input())
# print(bool(i // 100 == 0))

# 1. Функция trunc - является частью модуля math. Отсекает дробную часть от числа. Фактически, проще использовать встроенную функцию приведения типов int, так как её подгружать через модуль не нужно.
# Примеры:
# from math import trunc
# print(trunc(2.5)) # 2
# print(trunc(3.5)) # 3
# print(trunc(-2.5)) # -2
#
# print(int(2.5)) # 2
# print(int(3.5)) # 3
# print(int(-2.5)) # -2
#
# 2. Функция floor - является частью модуля math. Округляет числа в сторону минус бесконечности (вниз).
# Примеры:
# from math import floor
# print(floor(2.5)) # 2
# print(floor(3.5)) # 3
# print(floor(-2.5)) # -3
#
# 3. Функция ceil - является частью модуля math. Округляет числа в сторону плюс бесконечности (вверх).
# Примеры:
# from math import ceil
# print(ceil(2.5)) # 3
# print(ceil(3.5)) # 4
# print(ceil(-2.5)) # -2
#
# 4. Функция round - является встроенной функцией, которую не нужно подгружать. Она похожа на "школьное округление", но у неё есть своя особенность:
# Числа с дробной частью от 0 до 0.5 (не включая 0.5) - round округляет вниз.
# print(round(5.3)) # 5
# Числа с дробной частью от 0.5 (не включая 0.5) до 1 - round округляет вверх.
# print(round(6.7)) # 7
# Числа с дробной частью 0.5 - round округляет до ближайшего целого чётного числа.
# print(round(12.5)) # 12
# print(round(13.5)) # 14
#
# П.с.: "школьное" округление (если дробная часть от 0 до 0.5 (не включая 0.5) - округление вниз, а если от 0.5 до 1 - округление вверх) - это Российский стандарт и в Питон его не закладывали, поэтому приходится самим его реализовывать, вот код:
#
# from math import floor, ceil
# N = float(input())
# if N - int(N) < 0.5:
#     print(floor(N))
# else:
#     print(ceil(N))

# i = float(input())
# print(ceil(i / 10))

'''hello
blabla'''

print(ord('a'))  #номер в таблице ASCII

# input_string = input("Введите строку: ")
# print(*([input_string] * 4), sep=' ')

#S.ljust(width[, fillchar]).
#Метод  .ljust принимает один обязательный параметр width - ширину строки и один необязательный параметр fillchar
# - знак заполнителя (по умолчанию пробел) . Возвращает новую строку, в которой исходная строка S дополнена справа символами fillchar
# до указанной длины width. Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений:
d = 'qwerty'
print(d.ljust(10, '-'))

#S.rjust(width[, fillchar])
#S.center(width[, fillchar])

#S.zfill(width)
#Метод .zfill возвращает новую строку, в которой исходная строка S дополнена нулями слева так, чтобы длина новой строки стала равна width.

d = '123'
print(d.zfill(5))

# S.rstrip([chars])
# Метод  .rstrip возвращает копию строки, в которой справа удалены указанные символы (по умолчанию удаляются пробельные символы).
#S.lstrip([chars])

q = '  hello  '
print(q)
print(q.rstrip())
print(q.lstrip())

# S.rpartition(sep)
# Метод  .rpartition разбивает строку по последнему встреченному разделителю sep и возвращает кортеж, который состоит из трех элементов:
# строки до разделителя, самого разделителя и строки после разделителя.
# Если разделитель в строке отсутствует, то кортеж будет состоять из: двух пустых строк и исходной строки:
text = "Python is best"

print(text.rpartition('is '))
print(text.rpartition('not '))

s = "Python is best, isn't it"

print(s.rpartition('is'))

print('Hello\nworld\nhi\nbye')

a = [
    ['Семён', 'Семёнов', 32.56],
    ['Зоя', 'Иванова', 378],
    ['Катерина', 'Петрова', 65],
]

for name, mid_name, balance in a:
    text = f"""Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб."""
    print(text)


b = [6, 5, 2, 9]
print(sorted(b))
print(sorted(b, reverse=True))

a = [2, 5, 8, 99999]
b = [2, 5, 9]
print(a > b)

a = [2, 5, 9]
b = [2, 5, 9]
print(a == b)

# b = list(map(int, input('Введите значения: ').split()))
# print(f'Вот наш список: {b}')


#lang = input("Какой язык программирования будем учить?")

# match lang:
#     case "JavaScript":
#         print("Ты можешь стать фронтенд разработчиком")
#     case "Python":
#         print("Ты можешь стать Data Scientist-ом")
#
#     case "PHP":
#         print("Ты можешь стать бекенд разработчиком")
#
#     case "Solidity":
#         print("Ты можешь стать Blockchain разработчиком")
#
#     case "Java":
#         print("Ты можешь стать мобильным разработчиком")
#     case  _:
#         print("Язык не важен, главное уметь решать задачи)")

a = 'privet'
while len(a) > 0:
    print(a[0])
    a = a[1:]



input_string = input()
vowels = "AEIOUYaeiouy"
result = ""

for char in input_string:
    if char not in vowels:
        result += "." + char.lower()

print(result)



# def process_string(input_str):
#     vowels = "AEIOUYaeiouy"
#     result = ""
#
#     for char in input_str:
#         if char not in vowels:
#             result += "." + char.lower()
#
#     return result
#
#
# input_string = input()
# processed_string = process_string(input_string)
# print(processed_string)