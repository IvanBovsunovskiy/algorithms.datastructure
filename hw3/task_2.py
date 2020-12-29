"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

first_array = []
for ind in range(0, 13):
    first_array.append(randint(1, 100))

second_array = []
for ind in range(0, 13):
    if first_array[ind] % 2 == 0:
        second_array.append(ind)

print(f'First array: {first_array} \nSecond array: {second_array}')
