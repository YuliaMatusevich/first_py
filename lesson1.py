# number = 10000
# print(number)
# print(type(number))
# print(id(number))
#
# number1 = 10000
# print(number1)
# print(type(number1))
# print(id(number1))

# name = 'Bob'
# print(name)
# print(type(name))
# print(id(name))
#
# name1 = 'Bob'
# print(name1)
# print(type(name1))
# print(id(name1))

# print(5*2)
# print(5**2) # возведение в степень
# print(5+2)
# print(5-2)
# print(5/2) # деление, ответ 2,5
# print(5//2) # целочисленное деление, ответ 2
# print(5%2) # остаток от деления

name = input("What is your name? ")
# print('Hi ' + name)
print(f'Hi,{name}') # динамические переменные. типа string format

print(abs(-7))
c = [1, 3, 8, 0, 15]
c1 = len(c)
c2 = sum(c)
print(min(c))
print(max(c))

f = round((3.9)) #математическое округление
print(f)

str = 'hello '
print(len(str))
print(str * 5) #дублирует стринг заданное количество раз
print('e' in str)
print('e' not in str)
print(str[2])
print(str[0:3])#substring, inc 0, except 3 and further
print(str[::-1])# перевернет стринг задом наперед

s = ' hello world'
print(s.replace('e', 'a'))
print(s.split())
print((s.strip()))#Java trim
s1 = '123 hello world'
print((s1.strip('123')))
# s1.lstrip - слева
# s1.rstrip - справа

# islower, isupper - булеан проверяет регистр
# isdigit - булеан проверяет если это число
#isalpha - проверяет, что это только буквы
#isalnum - числа + буквы
#istitle - проверяет, начинается ли с большой буквы


