# num = 8
# if num == 5:
#     print("five")
# elif num == 7:
#     print("Seven")
# else:
#     print("Error")

# i = 0
# while i < 7:
#     i += 1
#     if i == 2:
#         continue
#     print(i)
#     if i == 4:
#         break


# y = 10
# while y > 0:
#     y -= 1
#     if y == 2:
#         continue
#     print(y)


# for i in range(10): #c 0 10 раз, т.е. до 9
#     print(i)
#
# for i in range(10, 100, 5):  #С, до не включая, шаг
#     print(i)
#
# print(bool(0))


# a = []
# if a:
#     print("True")
# else:
#     print("False")

# def sum(a,b):
#     return a + b
# print(sum(2,8))
#
# def power(y):
#     x = sum(2,3)
#     return x ** y
# print(power(2))

d = {1: "a", 2: "b", 3: "c"}
for key, value in d.items():
    print(f"{key} {value}")