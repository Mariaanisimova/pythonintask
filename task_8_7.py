# Задача 8. Вариант 7. 
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку. 

# Videneev P. A. 
# 26.05.2016 
import random 

WORDS = ("смерть", "луна", "эволюция", "монастырь", "крест", "воин", "акула") 

word = random.choice(WORDS) 
correct = word 

i_dont_know = "Не знаю" 
podskazka = word[0] + word[1] + word[2] 

jumble = "" 
while word: 
position = random.randrange(len(word)) 
jumble += word[position] 
word = word[:position] + word[(position + 1)☺ 

scores = 10 

print("""Привет ты в игре Анаграммы! 
Условия игры довольно просты, нужно переставить буквы так, чтобы получилось осмысленное слово. 
При затруднении с ответом воспульзуйтесь подсказкой, введите: "Не знаю". 
Предупреждаю, если вы не будете использовать подсказку, кол-во заработанных очков будет больше. 
(Для выхода нажмите Enter, не вводя своей версии.)""") 
print("Вот анаграмма: ", jumble) 
guess = input("\nПопробуйте отгадать исходное слово: ") 
while guess != "" and guess != correct: 
if guess != correct and not guess == i_dont_know: 
print("Неверный ответ") 
guess = input("\nПопробуйте отгадать исходное слово: ") 
if guess == i_dont_know: 
scores -= 5 
print("\nПодсказка! Первые три буквы слова!", podskazka) 
guess = input("Попробуйте отгадать исходное слово: ") 
if guess == correct: 
print("Верный ответ!\n") 


if scores < 0: 
scores = 0 
print("Благодарю за игру! У тебя", scores, "очков!") 
input("\n\nНажмите Enter для выхода")