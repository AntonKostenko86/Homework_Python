import math


def square(side):
    return math.ceil(side * side)


long_side = float(input("Введите длинну стороны квадрата: "))
print(f"Площадь квадрата = {square(long_side)}")
