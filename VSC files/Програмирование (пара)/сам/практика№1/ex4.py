"""
ex4.py

Код для решение третьего практического задания: 'сложные пароли'

Основные возможности:
    1. Генерировать пароль
    2. Выставлять настройки пароля:
        • Наличие нижнего регистра
        • Верхнего регистра
        • Спец символов
        • Цифр
        • Длинна пароля
    3. Приятный, понятный и красивый интерфейс терминала
"""

from string import ascii_lowercase, ascii_uppercase, digits
from random import choice

special_symbols = '!@#$%^&*-_=+№'

def password_generator():
    """
    Генерирует пароль основаясь на ответах пользователя
    
    Variables:
    upper_case_status (int) - проверяет нужны ли пользователю буквы в верхнем регистре
    lower_case_status (int) - проверяет нужны ли пользователю буквы в нижнем регистре
    special_symbol_status (int) - проверяет нужны ли пользователю спец. символы
    digit_status (int) - проверяет нужны ли пользователю цифры
    password_lenght(int) - хранит в себе кол-во символов желаемое пользлваетелем
    
    """    
    print('Запущен генератор пароля')
    upper_case_status = int(input('Нужен ли вам в вашем пароле верхний регистр?(1/0): '))
    if upper_case_status != 0:
        upper_case_status = 1
    if upper_case_status == 1:
        lower_case_status = int(input('Наличие нижнего регистра?(1/0): '))
        if lower_case_status != 0:
            lower_case_status == 1
    else:
        lower_case_status = 1
    special_symbol_status = int(input('Cпециальные символы?(1/0): '))
    if special_symbol_status != 0:
        special_symbol_status = 1
    digit_status = int(input('Наличие цифр?(1/0): '))
    password_lenght = int(input('Какова желаемая длина пароля?(8-45): '))
    if password_lenght > 45:
        password_lenght = 45
    if password_lenght < 8:
        password_lenght = 8
        
    characters = (ascii_lowercase * lower_case_status) + (ascii_uppercase * upper_case_status)\
        + (digits * digit_status) + (special_symbols * special_symbol_status)
    
    result = ''
    for position in range(1, password_lenght+1):
        result += choice(characters)

    print(f'Сгенерированный пароль: {result}')
    
password_generator()