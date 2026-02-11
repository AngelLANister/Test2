import math


def square(num):
    return math.ceil(num*num)


num = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(num)}")
