# 7. Проверка на палиндром
def is_palindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

print("'А роза упала на лапу Азора' - палиндром?", is_palindrome("А роза упала на лапу Азора"))

# Задача
