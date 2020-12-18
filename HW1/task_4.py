"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input("Please enter first letter from english alphabet: ").lower()
b = input("Please enter second letter from english alphabet: ").lower()

if (ord(a) in range(97,123)) and (ord(b) in range(97,123)):
    print(f"Letter {a} is {ord(a) - ord('a')+1} in alphabet and Letter {b} is {ord(b) - ord('a')+1} in alphabet,"
          f" between them is {abs(ord(a) - ord(b))-1} letters")
else:
    print('You entered symbol not from english alphabet')
