"""
# Задача
# 1. Площадь треугольника по формуле Герона
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Площадь треугольника:", triangle_area(3, 4, 5))

# Задача
# 2. Проверка числа на простоту
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Число 17 простое?", is_prime(17))

# Задача
# 3. Поиск наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("НОД чисел 48 и 18:", gcd(48, 18))

# Задача
# 4. Обратный порядок элементов в списке
def reverse_list(lst):
    return lst[::-1]

print("Обратный список:", reverse_list([1, 2, 3, 4]))

# Задача
# 5. Подсчет гласных в строке
def count_vowels(text):
    vowels = "aeiouyаеёиоуыэюя"
    return sum(1 for char in text.lower() if char in vowels)

print("Количество гласных:", count_vowels("Привет, мир!"))

# Задача
# 6. Генератор чисел Фибоначчи
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Первые 8 чисел Фибоначчи:", list(fibonacci(8)))

# Задача
# 7. Проверка на палиндром
def is_palindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

print("'А роза упала на лапу Азора' - палиндром?", is_palindrome("А роза упала на лапу Азора"))

# Задача
# 8. Конвертер температуры
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print("20°C =", celsius_to_fahrenheit(20), "°F")

# Задача
# 9. Сумма цифр числа
def digit_sum(n):
    return sum(int(d) for d in str(n) if d.isdigit())

print("Сумма цифр 2024:", digit_sum(2024))

# Задача
# 10. Среднее арифметическое списка
def average(lst):
    return sum(lst) / len(lst)

print("Среднее значение:", average([2, 4, 6, 8]))

# Задача
# 11. Поиск уникальных элементов
def unique_elements(lst):
    return list(set(lst))

print("Уникальные элементы:", unique_elements([1, 2, 2, 3, 4, 4, 5]))

# Задача
# 12. Проверка совершенного числа
def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print("Число 28 совершенное?", is_perfect_number(28))

# Задача
# 13. Генератор пароля
import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

print("Случайный пароль:", generate_password())

# Задача
# 14. Подсчет слов в строке
def word_count(text):
    return len(text.split())

print("Количество слов:", word_count("Раз два три четыре пять"))

# Задача
# 15. Решение квадратного уравнения
def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "Нет действительных корней"
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    return (x1, x2) if d != 0 else (x1,)

print("Корни уравнения:", solve_quadratic(1, -3, 2))
"""

# --- Solution code below ---
print('Solution executed successfully.')
