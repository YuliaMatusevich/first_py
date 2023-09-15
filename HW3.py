# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0], my_list[2][1], my_list[2][2])

# Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#  - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
for i in list_1:
    if isinstance(i, str) and 'a' in i:
        print(i)

# Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list = ['cat', 'dog', 'horse', 'cow']
tuple = tuple(list)
print(tuple)


# Напишите программу, которая определяет, какая семья больше.
#  1) Программа имеет два input() - например, family_1, family_2.
#  2) Членов семьи нужно перечислить через запятую.
# Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# def countFamily():
#     family_1 = input("Please enter F1 names: ").split(',')
#     family_2 = input("Please enter F2 names: ").split(",")
#
#     if len(family_1) > len(family_2):
#         print(family_1)
#     elif len(family_1) < len(family_2):
#         print(family_2)
#     else:
#         print("Equal")
#
#
# countFamily()

# Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
# о вашем любимом фильме.
# - распечатайте только ключи
# - распечатайте только значения
# - распечатайте пары ключ - значение

dict = {'title': 'Nebo',
        'director': 'Ivan',
        'year': 1990,
        'budget': 2000000,
        'main_actor': 'Anna',
        'slogan': 'never give up'}
print(dict.keys())
print(dict.values())
print(dict.items())

#Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

print(sum(my_dictionary.values()))

#Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
listList = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(listList))

#Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     # - найдите значения, которые встречаются в обоих множествах
     # - найдите значения, которые не встречаются в обоих множествах
     # - проверьте являются ли эти множества подмножествами друг друга

print('**********************************************')
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

set3 = set()
for i in set1:
    if i in set2:
        set3.add(i)
print(set3)

print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))