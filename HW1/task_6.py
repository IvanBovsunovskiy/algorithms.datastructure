"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

try:
    [a, b, c] = input("Please enter length of the triangle sides (a, b, c): ").split(',')
    print(a, b, c)
    a = float(a)
    b = float(b)
    c = float(c)
except (TypeError, ValueError):
    print("You entered wrong sides' lengths")
else:
    if a > 0 and b > 0 and c > 0:
        if a == b and a == c and b == c:
            print("Triangle is equilateral triangle")
        elif a == b or a== c or b == c:
            print("Triangle is isosceles triangle")
        elif a + b > c and b + c > a and c + a > b:
            print("Triangle is regular.")
        else:
            print("Triangle can not have such sides with such lengths")
    else:
        print("Triangle can not have such sides with such lengths")
