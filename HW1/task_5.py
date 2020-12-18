"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

try:
    a = int(input("Please enter letter number from english alphabet: "))
except (TypeError, ValueError):
    print("You entered wrong letter number")
else:
    if a in range(1,27):
        print(f"Letter with number {a} is {chr(a + 96)}")
    else:
        print('You entered number not from english alphabet')
