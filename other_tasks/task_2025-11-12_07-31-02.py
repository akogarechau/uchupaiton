# 9. Сумма цифр числа
def digit_sum(n):
    return sum(int(d) for d in str(n) if d.isdigit())

print("Сумма цифр 2024:", digit_sum(2024))

# Задача
