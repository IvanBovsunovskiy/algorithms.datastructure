"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""

year = int(input("Please enter year(positive integer): "))
if not (year % 4):
    check = True
    if not(not(year % 100) and year % 400):
        check = True
    else:
        check = False
else:
    check = False

if check:
    print("Was entered leap year")
else:
    print("Entered year is NOT leap")
