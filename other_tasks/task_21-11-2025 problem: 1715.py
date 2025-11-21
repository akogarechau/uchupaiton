# 3. Поиск наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("НОД чисел 48 и 18:", gcd(48, 18))

# Задача
