﻿# Задача 4 Вариант 39
# Напишите программу, которая выводит имя, под которым скрывается Евгений Петрович Катаев. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.
# Короткова Дарья Сергеевна
# 17.03.2016
print ('Евгений Петрович Катаев известен, как Евгений Петрович Петров, он является русским советским писателем, журналистом, сценаристом. Соавтор Ильи Ильфа. Главный редактор журнала "Огонёк" c 1938 года.')
print ('Место Рождение: Одесса,Российская империя')
a=1902
b=1942
v=b-a

print ('Год рождения: ' + str(a))
print ('Год смерти: ' + str(b))
print ('Возраст: ' + str(v))
print ('Область интересов: русский советский писатель, журналист, сценарист')

input ('Нажмите Enter для выхода.')