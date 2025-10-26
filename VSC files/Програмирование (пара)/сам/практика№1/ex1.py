"""
ex.py 

Код для решение первого практического задания: 'Шифр Цезаря'

Основные возможности:
- Шифровать текст
- Дешифровать текст
- Работает как с русским языком, так и с английским
- Автоматически определяет язык входного текста
"""

# получаем английский алфавит
from string import ascii_lowercase

def encrypt(str: str, shift: int):
    """
    Шифрует заданную строку методом Цезаря

    Args:
        str (str): строка которая будет зашифрована
        shift (int): сдвиг по методу Цезаря

    Returns:
        str: зашифрованная строка
    """
    
    result = '' # переменная, в которую будет записана зашифрованная строка
    

    for char in str: # перебираем каждый символ строки
        if char.isalpha(): # проверяем буква ли это
            
            # проверка на регистр буквы
            case_flag = 0
            if char.isupper() == 1:
                case_flag = 1
                
            # проверяем из на принадлежание анг. алфавиту, если истина - шифруем
            if char.lower() in ascii_lowercase:
                result += chr(((ord(char.lower()) + shift - ord('a')) % 26 + ord('a'))\
                              + ((ord('A') - ord('a')) * case_flag))

            # шифруем с учетом проверки алфавита
            else:
                result += chr(((ord(char.lower()) + shift - ord('а')) % 32 + ord('а'))\
                              + ((ord('А') - ord('а')) * case_flag))
        
        # в случае если char не являлся буквой - не меняем его
        else:
            result += char
      
    return result

def decrypt(str: str, shift: int):
    """
    дешифрует код, используя функцию шифрования, 
    но заменяя shift обратным по знаку

    Args:
        str (str): строка которую нужно дешифровать
        shift (int): сдвиг по методу Цезаря

    Returns:
        str: расширофванная строка
    """    
    return encrypt(str, -shift)