# 6. Генератор чисел Фибоначчи
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Первые 8 чисел Фибоначчи:", list(fibonacci(8)))

# Задача
