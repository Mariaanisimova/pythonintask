#Задача 8. Вариант 1.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Anisimova M.L.
# 27.09.2016

import random

WORDS = ("семестр", "компьютер", "программа", "зачёт", "экзамен", "университет")
word = random.choice(WORDS)
correct = word
 
i_dont_know = "подсказка"
riddle = word[0] + word[1] + word[2]
 
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
 
scores = 100

print("""Вы принимаете участие в игре Анаграммы!Вам следует переставить буквы так, чтобы получилось осмысленное слово. Если вам нужна подсказка введите: "подсказка", Но если вы не будете использовать подсказку, кол-во заработанных очков будет больше.
     
(Для выхода из игры нажмите Enter, не вводя своей версии загаданного вам слова.)""")

print("Слово, которое мы для вас загадали в игре Анаграммы: ", jumble)
guess = input("\nПопробуйте отгадать данное вам слово: ")
while guess != "" and guess != correct:
    if guess != correct and not guess == i_dont_know:
        print("К сожалению вы не угадали. Попробуй еще раз.")
        guess = input("\nПопробуйте отгадать данное вам слово: ")
    if guess == i_dont_know:
        scores -= 10
        print("\nВот вам подсказка! Первые три буквы слова!", riddle)
        guess = input("Попробуйте отгадать данное слово: ")
    if guess == correct:
            print("Да, Правильно!Вы угадали!!!\n")
 

if scores < 0:
    scores = 0
print("Спасибо большое за игру! Ждём вас вновь и в итоге у вас", scores, "очков!")
input("\n\nНажмите ENTER, чтобы завершить") 
