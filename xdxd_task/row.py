import sys

sys.set_int_max_str_digits(0)


def get_nth_digit(position):
    """
    Находит n-ю цифру в конкатенации всех натуральных чисел:
    123456789101112131415...
    """
    num_digits = 1
    numbers_count = 9

    # Находим блок чисел с нужным количеством цифр
    while position > num_digits * numbers_count:
        position -= num_digits * numbers_count
        num_digits += 1
        numbers_count *= 10

    # Вычисляем номер числа в текущем блоке и позицию цифры
    target_number = (numbers_count // 9) + (position - 1) // num_digits
    digit_index = (position - 1) % num_digits

    return str(target_number)[digit_index]


def pretty_print_result(n, digit):
    """вывод результата"""
    print(f"\n{'='*50}")
    print(f"    Позиция: {n:,}")
    print(f"    Цифра: '{digit}'")
    print(f"{'='*50}\n")


# Основная программа
if __name__ == "__main__":
    try:
        n = int(input("   Введите номер позиции (n): "))
        if n < 1:
            raise ValueError("Позиция должна быть положительной!")
            
        result_digit = get_nth_digit(n)
        pretty_print_result(n, result_digit)
