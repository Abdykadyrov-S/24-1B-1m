# num = 12 , 1.3, False

# print(num)
# print(type(num))


# numbers = [1,2,3,4,5,6,7,8,9,10]

# for num in numbers:
#     if num%2== 0:
#         print(num)


# for i in range(2, 11, 2):
#     print(i)

# for i in range(10):
#     print("hello world")

"break - остановить цикл (выйти из цикла)"

"continue - прерывает текущую итерацию и переходит на новую"


"while - бесконечный цикл"

# if True:
#     print("Hello world")

# print(5 > 3)

"""
while - пока

while - пока условие правильное

while True:

while 5 > 3:

"""

# while 5 > 3:
#     print("5 > 3")

# if 5 > 3:
#     print("5 > 3")


# while True:
#     print("5 > 3")

# while False:
#     print("5 > 3")


# number = 3
# while 5 > number:
#     # number = number + 1
#     number += 1
#     print("Hello world")

# while True:
#     num = int(input("Введите число: "))

#     if num == 0:
#         print("Выход")
#         break

#     if num == 7:
#         print("Неправильное значение")
#         continue

#     if num%2== 0:
#         print("четное")
#     else:
#         print("Нечетное")


import random

# num = random.randint(1,100)
# # random integer
# print(num)

# my_list = ['Adelina', 'Nuraziz', 'Kudbuhon']
# name = random.choice(my_list)
# print(name)


count = 0
number = random.randint(1,50)
while True:
    count += 1
    user_num = int(input("Введите число от 1-50: \n:"))
    
    if user_num > number:
        print("Загаданное число меньше")
    elif user_num < number:
        print("Загаданное число больше")
    else:
        print(f"Вы угадали число {number} за {count} попыток")
        break

