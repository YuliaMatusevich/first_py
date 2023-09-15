# #LISTS  - ИЗМЕНЯЕМАЯ СТРУКТУРА
#
# lst = [10, 'Hello', None, True, 25.25, 154, -6]
# print(lst)
# print(lst[2])
# print(lst[-1])
# print(len(lst))
# print(id(lst))
#
# lst.append('Python')  #добавляет в конец списка, список остаётся тот же ID
# print(lst)
# print(id(lst))
#
# lst.insert(1, 'Hi')  #добавляет на определенный индекс значение, список остаётся тот же ID
# print(lst)
# print(id(lst))
#
# lst.reverse()  #разворачивает задом наперед, список остаётся тот же ID
# print(lst)
# print(id(lst))
#
# lst1 = []
# for i in lst:
#     if isinstance(i, int):
#         lst1.append(i)
# #True = превращается в 1
# print(lst1)
# print(sum(lst1))
# print(min(lst1))
# print(max(lst1))
#
# #.index(), .clear(), .remove(), .count()
#
# print(lst.count(True))
# print(lst.index(10)) #если будет несколько раз, то напишет индекс первого встретившегося
#
# #LIST COMPREHENSION
# #NEWLIST = [EXPRESSION for ITEM in ITERABLE if CONDITION == TRUE]
#
# list = [1, 20, 8, 4, 5]
# new_list = [x * x for x in list if x % 2 == 0]
# print(new_list)

# list.sort()        # изменит первоначальный список
# print(list)

# list11 = sorted(list)  # не изменит первоначальный список
# print(list11)

 ##################################################################################################

#TUPLES - НЕИЗМЕНЯЕМЫЕ СТРУКТУРЫ

# my_tuple = (1, True, None, 'Hello')
# print(type(my_tuple))
# print(my_tuple)
#
# my_tuple1 = 1, 'hello', False
# print(type(my_tuple1))
# print(my_tuple1)
#
# list3 = list(my_tuple)
# print(list3)
#
# print(tuple(list3))
#
# def sum_it(*args):
#     return sum(args)
#
# print(sum_it(1, 8, -3))

#.index(), .count(), sum(), min(), max(), len()

#####################################################################################################

#DICTIONARY

dict = {'name': 'Anna',
        'last_name' : 'Brown',
        'age' : 30,
        'position': 'QA'}
print(dict)
print(dict['position'])

dict['age'] = 31
print(dict)

# .keys(), .items(), .get(), .clear(), .copy(), len(), type(), min(), max()
print(dict.keys())
print(dict.items())
print(dict.get('name'))
dict1 = dict.copy()
print(dict1)

print(min(dict1))

def keywords(**kwargs):
    return kwargs

print(keywords(name = 'Alice', age = 40))


###################################################################################################
#SETS (множества)
#только уникальные значения

my_set = {1, 2, 5, 8, 4, 2, 1}
print(my_set)

#.len()
# x in s
#set.add()
#set.remove()
#set.pop() - удаляет первый элемент из множества
#set.clear()
#set.issubset(other)  -  все элементв set принадлежат other
#set.issuperset(other)  -  все элементы other принадлежат set

set1 = {1, 2, 3, 'one', 'ten'}
set2 = {1, 2, 3}

print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.difference(set2))

set1.remove(1)
print(set1)

set1.add(9)
print(set1)


################################################################

list_list = [5, ['a', 'b', 'c'], True]
print(list_list[1][2])

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.insert(5, 111)

numbers1 = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
print(numbers1.sort(reverse=True))

# Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом,
# чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы
#Бросай курить
#Б-Р-О-С-А-Й К-У-Р-И-Т-Ь

# Получаем ввод от пользователя
input_string = input()

# Преобразуем каждое слово в верхний регистр и добавляем дефисы между буквами
words = input_string.split()
transformed_words = []

for word in words:
    upper_case_word = word.upper()
    word_with_hyphens = '-'.join(upper_case_word)
    transformed_words.append(word_with_hyphens)

# Объединяем преобразованные слова в одну строку через пробел
result = ' '.join(transformed_words)

# Выводим результат
print(result)
