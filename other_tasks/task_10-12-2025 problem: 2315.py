# 15. Решение квадратного уравнения
def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "Нет действительных корней"
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    return (x1, x2) if d != 0 else (x1,)

print("Корни уравнения:", solve_quadratic(1, -3, 2))
