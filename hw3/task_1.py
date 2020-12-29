"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

multiplicity_array = [[2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0]]
for temp in range(2, 100):
    for ind in range(0, 8):
        if temp % multiplicity_array[0][ind] == 0:
            multiplicity_array[1][ind] += 1
string_answer = f''
for ind in range(0, 8):
    string_answer = string_answer + f'{multiplicity_array[1][ind]} numbers are multiples of {multiplicity_array[0][ind]} \n'
print(string_answer)

