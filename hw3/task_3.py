"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

array = []
for ind in range(0, 13):
    array.append(randint(1, 100))

print(f'Current array: {array}')
max_in_array = [max(array), array.index(max(array))]
min_in_array = [min(array), array.index(min(array))]
array.remove(max_in_array[0])
array.insert(min_in_array[1], max_in_array[0])
array.remove(min_in_array[0])
array.insert(max_in_array[1], min_in_array[0])
print(f'Modified array: {array}')
