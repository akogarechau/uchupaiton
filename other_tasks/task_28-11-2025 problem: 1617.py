# 12. Проверка совершенного числа
def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print("Число 28 совершенное?", is_perfect_number(28))

# Задача
