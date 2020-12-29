"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

from random import randint

array = []
for ind in range(0, 15):
    array.append(randint(-100, 100))

max_negative_element = []

for temp in array:
    if temp < 0:
        if not max_negative_element or temp > max_negative_element:
            max_negative_element = temp

print(f'Initial array: {array}')
print(f'Maximal negative element is: {max_negative_element} with position {array.index(max_negative_element)}(from 0)')
