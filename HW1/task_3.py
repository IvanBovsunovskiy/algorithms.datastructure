"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

try:
    a = input("Please enter lower bound for random integer: ")
    a = int(a)
    b = input("Please enter upper bound for random integer: ")
    b = int(b)
except (TypeError, ValueError):
    print("You entered wrong integer numbers")
else:
    if a < b:
        print(f"Random integer in range [{a},{b}] is - {random.randint(a,b)}")
    else:
        print("You entered wrong integer numbers")

try:
    a = input("Please enter lower bound for random real: ")
    a = float(a)
    b = input("Please enter upper bound for random real: ")
    b = float(b)
except (TypeError, ValueError):
    print("You entered wrong real numbers")
else:
    if a < b:
        print(f"Random real in range [{a},{b}] is - {random.uniform(a,b)}")
    else:
        print("You entered wrong integer numbers")

try:
    a = input("Please enter lower bound for random real: ")
    a = ord(a)
    b = input("Please enter upper bound for random real: ")
    b = ord(b)
except TypeError:
    print("You entered wrong symbols numbers")
else:
    if a > b:
        [a, b] = [b, a]
    print(f"Random symbol from UTF-8 in range [{chr(a)},{chr(b)}] is - {chr(random.randint(a,b))}")
