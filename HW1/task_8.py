"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = float(input("Please enter first number: "))
b = float(input("Please enter second number: "))
c = float(input("Please enter third number: "))

if (b < a < c) or (b > a > c):
    print(f'number {a} is between numbers {b} and {c}')
elif (a < b < c) or (a > b > c):
    print(f'number {b} is between numbers {a} and {c}')
elif (a < c < b) or (a > c > b):
    print(f'number {c} is between numbers {a} and {b}')
else:
    print('Some of numbers is equal.')
