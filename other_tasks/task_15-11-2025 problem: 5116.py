# 5. Подсчет гласных в строке
def count_vowels(text):
    vowels = "aeiouyаеёиоуыэюя"
    return sum(1 for char in text.lower() if char in vowels)

print("Количество гласных:", count_vowels("Привет, мир!"))

# Задача
