
#  Алгоритм для определения, является ли строка палиндромом
# 1. Удаление пробелов и приведение к одному регистру:
#    - Удалить все пробелы из строки.
#    - Привести строку к нижнему регистру (или верхнему).
# 2. Сравнение символов:
#    - Определить длину строки.
#    - Сравнить символы с начала строки и с конца:
#      - Если символы не равны, строка не является палиндромом.
#      - Если все символы равны до середины строки, то строка является палиндромом.
# 3. Вывод результата:
#    - Если строка является палиндромом, вернуть `True`, иначе вернуть `False`.
#


def is_palindrome(s):
    # Шаг 1: Удаляем пробелы и приводим к нижнему регистру
    cleaned_str = ''.join(s.split()).lower()

    # Шаг 2: Сравниваем символы
    length = len(cleaned_str)
    for i in range(length // 2):
        if cleaned_str[i] != cleaned_str[length - 1 - i]:
            return False  # Не палиндром

    # Шаг 3: Если все символы совпали, то это палиндром
    return True  # Палиндром

# Примеры использования
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))                         # False
print(is_palindrome("Racecar"))                       # True
print(is_palindrome("А роза упала на лапу Азора"))    # True
print(is_palindrome("Если все символы совпали"))      # False