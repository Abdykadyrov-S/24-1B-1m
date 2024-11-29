import random

words = ['mersedes-benz', 'subaru', 'audi', 'ferrari', 'toyota', 'porsh','temirlan',]
word = random.choice(words)

word_letters = []
attempts = 6
print("Добро пожаловать в игру 'ПОЛЕ ЧУДЕС'!")
print("У вас есть 6 попыток, чтобы угадать слово.")
while attempts > 0: 
    hidden_word = ''
    for letter in word:
        if letter in word_letters:
            hidden_word += letter
        else:
            hidden_word += '_'
    print("Загаданное слово:", hidden_word)
    print("Оставшиеся попытки:", attempts)
    user = input("Введите букву: ").lower()
    if user in word_letters:
        print("Вы уже угадали эту букву. Попробуйте другую.")
        continue
    word_letters.append(user)
    if user not in word:
        attempts -= 1
        print("Буква", user, "не входит в загаданное слово.")
    if '_' not in hidden_word:
        print("Поздравляю! Вы угадали слово:", word)
        break
# if attempts == 0:
else:
    print("Вы проиграли! Загаданное слово было:", word)