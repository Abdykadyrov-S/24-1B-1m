"Арифметические операции. Переменные."

# print(2 + 2)
# print(2 - 2)

# print(3 * 2)
# print(3 ** 2) # 3 * 3
# print(3 ** 3) # 3 * 3 * 3

# print(2 / 2) # Деление (вывод с остатком)
# print(7 // 2) # Деление (вывод без остатка)

# print(2 % 2)


"Операции сравнения"

# # больше чем - >
# print(6 > 3)

# # меньше чем - <
# print(6 < 3)

# # равно - ==
# print(6 == 6)

# # знак присваивания - =
# a = 5

# # не равно - !=
# print(6 != 5)

# # больше или равно - >=
# print(6 >= 7)

# # меньше или равно - >=
# print(6 <= 7)




"комментарий"
# 
"""
комментарий
комментарий
комментарий

"""

''
''''''






"Регистр"

# name = "Mark"
# reg = "нижний регистр"

# NAME = "Mark"
# REG = "ВЕРХНИЙ РЕГИСТР"

# snake_case = "змеиный_регистр"
# CamelCase = "ВерблюжийРегистр"

text = """
Advertising companies say advertising is necessary and important. 
It informs people about new products. 
Advertising hoardings in the street make our environment colourful. 
And adverts on TV are often funny. Sometimes they are mini-dramas 
and we wait for the next programme in the mini-drama. Advertising 
can educate, too. Adverts tell us about new, healthy products. 
And adverts in magazines give us ideas for how to look prettier, 
be fashionable and be successful. Without advertising, life is 
boring and colourless.

But some consumers argue that advertising is a bad thing. 
They say that advertising is bad for children. Adverts make 
children ‘pester’ their parents buy things for them. Advertisers 
know we love our children and want to give them everything. 
So they use children’s ‘pester power’ to sell their products. 
Finally, consumers say, if there is advertising there must be rules. 
Some adverts advertise unhealthy things like cigarettes and make 
people waste their money
"""

# print(text)

"Типы данных"

# print(5)
# print("5")

"""
INTEGER - целые числа
int()
"""
number = 125
age = 16

"""
FLOATING - числа с плавающей запятой
float()
"""
pi = 3.14
number = 12.5

"""
BOOLEAN - логический тип данных
bool()
"""

is_student = True 

is_married = False 

"""
STRING - строка
str()
"""
number = "125"
adress = "М.Аматова 1"
'''Привет группа 24-1B'''


# num = 7
# num = 5
# print(num)


# name = 'Кутя и Нуразиз'
# #       0123456789

# "срезы" 
# """
# [начало:конец:шаг]
# [1]
# [1:3]

# """
# print(name[3])
# print(name[1:3])
# print(name[:])
# print(name[:4])
# print(name[7::3])

# mentor = "Adelina"

# name = 'Кутя , Нуразиз и {0} '.format(mentor)
# name_2 = f'Кутя , Нуразиз и {mentor}'

# print(name)
# print(name_2)

num1 = 2
# num2 = 5

# print(f"{num1} + {num2} = {num1 + num2}")


"Конкантенация"
"""
Конкантенация - это склеивание строк через оператор  +
"""

# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
# print(f"{num1} + {num2} = {num1 + num2}")

# number = '125 and 45'

# print(int(number) + 25)



# text = """
# Конкантенация - это склеивание строк через оператор  +
# """

# a = text.count('к')
# b = text.count('К')

# print(a + b)


# text = """
# Конкантенация - это склеивание строк через оператор  +
# """.upper()

# print(text)
# print(text.count("К"))