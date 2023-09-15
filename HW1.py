# //Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# Пример:
#
# Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8

number = int(input('Enter a number: '))
thousand = number // 1000
hundred = number % 1000 // 100
dozens = number % 100 // 10
units = number % 10
print(f'Тысячи - {thousand}')
print(f'Сотни - {hundred}')
print(f'Десятки - {dozens}')
print(f'Единицы - {units}')
ч