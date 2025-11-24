# 1. Площадь треугольника по формуле Герона
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Площадь треугольника:", triangle_area(3, 4, 5))

# Задача
