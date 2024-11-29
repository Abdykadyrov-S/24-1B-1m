"Условия. Ветвления в Python"

"Условная конструкция. Условные операторы"

"""
if - оператор, который создает усл. конструкцию

elif - оператор, который продолжает усл. конструкцию

else - иначе(заканчивает усл.конструкцию)

"""


"""
if условие:
    код который относится к условию 

if True:
    сработает
"""

num_1 = 6
num_2 = 5

# if num_1>num_2:
#     print('первое число больше')
# elif num_2<num_1:
#     print('второе число больше')
# elif num_2==num_1:
#     print('числа равны')
# elif num_1>num_2:
#     print('числа равны')
# else:
#     print('числа равны')


# if num_1>num_2:
#     print('первое число больше')
# if num_2<num_1:
#     print('второе число больше')
# if num_2==num_1:
#     print('числа равны')
# if num_1>num_2:
#     print('числа равны')
# else:
#     print('числа равны')


# age = int(input("Введите возраст: "))

# if age <= 12:
#     print("Проходите дальше")
# else:
#     print("Вам нельзя")


login = "Geeks Adelina Nurbek Aziz"
password = "2021"

# user_login = input("Введите логин: ")
# user_password = input("Введите пароль: ")

# if login == user_login:
#     print("Доступ разрешен")
# elif password == user_password:
#     print("Доступ разрешен")

# if login == user_login:
#     user_password = input("Введите пароль: ")
#     if password == user_password:
#         print("Доступ разрешен")
#     else:
#         print("Неправильный пароль")
# else:
#     print("Такого пользователя не сущ.")

"""
and, or, in, not in
"""

# if login == user_login and password == user_password:
#     print("Доступ разрешен")
# else:
#     print("Неправильный пароль или логин")

# if login == user_login or password == user_password:
#     print("Доступ разрешен")
# else:
#     print("Неправильный пароль или логин")


"in, not in"
# if user_login in login:
#     user_password = input("Введите пароль: ")
#     if password == user_password:
#         print("Доступ разрешен")
#     else:
#         print("Неправильный пароль")
#         choice = input("Хотите сбросить пароль?: ")
#         if choice == '+':
#             "логика"
#         elif choice == '-':
#             pass

# else:
#     print("Такого пользователя не сущ.")

# num = 5
# if 4 < num < 10:
#     "НЕ ТРОГАТЬ - еще не дописал(еще не придумал)"
#     pass



num = int(input("Введите число: "))

if num%2== 0:
    print("четное")
