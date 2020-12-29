"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

array = []
for ind in range(0, 15):
    array.append(randint(1, 100))

ind = 0
frequent_number = []
iterations = len(array)

while True:
    if not ind:
        frequent_number = [array.count(array[ind]), array[ind]]
    elif frequent_number[1] != array[ind]:
        if array.count(array[ind]) > frequent_number[0]:
            frequent_number[0:2] = [array.count(array[ind]), array[ind]]
            while len(frequent_number) > 2:
                frequent_number.pop()
        elif array.count(array[ind]) == frequent_number[0] and not(array[ind] in frequent_number[1:]):
            frequent_number[0:1] = [array.count(array[ind]), array[ind]]
    ind += 1
    if ind > iterations - 1:
        break
print(f'Initial array: {array}')
print(f'The most often({frequent_number[0]} times) in array is/are the following number/s: {frequent_number[1:]}')
