﻿# Задача 6.
# Создайте игру, в которой компьютер загадывает название одного из семи холмов, на которых по легенде XVI века была #построена Москва, а игрок должен его угадать.
# Danilenkov M.A.

import random

holmi = ("Боровицкий холм", "Псковская гора", " Таганский холм", "Ивановская горка", "Красный холм","Старо-Ваганьковский холм", "Чертольский холм".)
zagadka = random.choice(holmi)
predpologenie = input("Программа загадала один из семи холмов, на которых по легенде XVI века была построена Москва \nВаш ответ: ")
if predpologenie.lower() == zagadka.lower():
    print("Молодец")
else:
    print ("Неправильно\nПравильный ответ - " + zagadka)

input("\n\nВведите ENTER для выхода")