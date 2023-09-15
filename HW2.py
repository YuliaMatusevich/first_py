# #Task1
# health = (int)(input("Enter your health points: "))
# if health <= 0:
#     print("False")
# else:
#     print("True")
#
#
# #Task2
# number = (int)(input("Enter a number: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


#Task3
#Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

# year = (int)(input("Enter a year: "))
# if year % 400 == 0:
#     print("Високосный")
# elif year % 100 == 0:
#     print("Не вискокосный")
# elif year % 4 == 0:
#     print("Високосный")
# else:
#     print("Не висконосный")

#Task4
#Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# def printTextNTimes():
#     text = (input("Enter a text: "))
#     times = (int)(input("Enter a number: "))
#     print(text * times)
#
# printTextNTimes()


# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере.
# Пробелы, знаки препинания, заглавные и строчные буквы важны!
#
# Входные данные
# Вводится целое число, по модулю не превосходящее 10000.
#
# Выходные данные
# Выведите сначала фразу "The next number for the number ", затем введенное число, затем слово " is ",
# окруженное пробелами, затем формулу для следующего за введенным числа, наконец, знак точки без пробела.
# Аналогично в следующей строке для предыдущего числа.
#
# Sample Input:
# 179
# Sample Output:
# The next number for the number 179 is 180.
# The previous number for the number 179 is 178



def printNextPreviousNumber():
    number = int(input("Please enter a number in the interval -10000 to 10000: "))
    if abs(number) > 10000:
        print(f"Number {number} is out of the limit. Please try again.")
    else:
        print(f'The next number for the number {number} is {number + 1}.')
        print(f'The previous number for the number {number} is {number - 1}.')

printNextPreviousNumber()

#
# number = int(input("Please enter a number in the interval -10000 to 10000: "))
#
# next_or_prev = "next" if number >= 0 else "previous"
# number = abs(number)
#
# print(f"The {next_or_prev} number for the number {number} is {number + 1 if next_or_prev == 'next' else number - 1}.")

