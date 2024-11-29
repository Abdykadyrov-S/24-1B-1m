"Dict - Словари"
"dict()"

# my_list = [12, "qwerty", True]
# #          0       1      2

# my_dict = {'number': 12, 'text': "qwerty",'bool': True}
# #значения:           1              2             3
# my_dict['text'] = ['q', 'w', 'e']

# print(my_list[0])
# print(my_dict['text'])
# print(my_dict)

# student = dict(name="Аслан", full_name="Байбалаев")

# print(student)

# del student['full_name']
# print(student)


# my_dict = {'number': 12, 'text': "qwerty",'bool': True}

# print(my_dict['text'])
# print(my_dict.get('key_1', 'No key'))
# print("Hello world")
# print(my_dict.setdefault('key_1', 'value_1'))
# print(my_dict)


# my_dict = {'number': 12, 'text': "qwerty",'bool': True}

# print(my_dict.keys())


# print(my_dict.values())


# print(my_dict.items())


"Множества в Python (set, frozenset)"

# my_set = {12, 23, 'a', 'g', True, 12, 'g'}
# numbers = {5, 2, 9, 1, 3,4, 2, 6, 7, 8, 9, 7} 

# print(type(my_set))
# print(my_set)
# print(numbers)

# my_frozenset = frozenset(numbers)
# print(type(my_frozenset))
# print(my_frozenset)

# numbers = [5, 2, 9, 1, 3,4, 2, 6, 7, 8, 9, 7]

# print(numbers)

# numbers = frozenset(numbers)
# print(numbers)

# my_list = [12, "qwerty", True, 32, 12, 'qwerty']
# print(my_list)

# my_list = set(my_list)
# # print(my_list)

# my_list = list(my_list)
# print(my_list)

# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]

# res = a + b

# print(res)


# my_set = {1, 3, 67, 123, 24, 12, 23, 234, 67, 12, 98, 100}
# print(my_set)


"""Циклы

Циклы предназначены для повторения определенного кода 
и для перебора значений в итерируемых типах данных
"""

"""
for 

while 
"""

"""
for новое_переменное in итерируемый тип данных:
    код который будет повторятся
    тело цикла

for новое_переменное in range(1, 5)
for новое_переменное in range(5)
"""

# for i in range(1, 10):
#     print(f"{i}) Hello world")
    
# for i in range(1, 10):
#     if i%2 == 0:
#         print(f"{i}) Hello world")

# my_str = 'text'
# for letter in my_str:
#     print(letter)
    # letter = 't'
    # letter = 'e'
    # letter = 'x'
    # letter = 't'

# print(letter)

students = ['Мухаммедали', 'Байэл', 'Амирхан', 'Хусеин', 'Салават', 'Дуйшобек', 'Мира']
# for student in students:
#     print(student, end=", ")

# number = 125
# for num in number:
#     print(num)

# count = 0
# for student in students:
#     # count = count + 1
#     count += 1
#     print(student)
#     if student == 'Амирхан':
#         break


# count = 0
# for student in students:
#     # count = count + 1
#     count += 1
#     print(student)
#     if student == 'Амирхан':
#         continue

#     print(f"Привет {student}")


kutya = {'name': "Kudbuhon", 'age':16, 'hobby': "bulling"}

# for i in kutya:
#     print(i)

# for i in kutya.keys():
#     print(i)

# for i in kutya.values():
#     print(i)

# for i in kutya.items():
#     print(i)

# for b, a in kutya.items():
#     print(f"{a} - {b}")

