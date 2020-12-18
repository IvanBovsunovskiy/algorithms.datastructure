"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

try:
    [x1, y1] = input("Please enter coordinates of the first point in the following: x1, y1 ").split(",")
    x1 = float(x1)
    y1 = float(y1)
except TypeError:
    print('You entered wrong data')
else:
    try:
        [x2, y2] = input("Please enter coordinates of the first point in the following: x2, y2 ").split(",")
        x2 = float(x2)
        y2 = float(y2)
    except TypeError:
        print('You entered wrong data')
    else:
        print(f"Line equation is y = {(y2 - y1) / (x2 - x1)} * x + {y2 - (y2 - y1) / (x2 - x1) * x2}")
finally:
    print('END')
