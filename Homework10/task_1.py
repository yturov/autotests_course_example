# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name():
    """
    Генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    """
    while True:
        letters = string.ascii_lowercase  # Генерим строку с буквами в нижнем регистре
        list_string = []  # Создаем пустой список
        for i in range(2):
            len_string = random.randint(1, 15)  # Генерим случайное целое число от 1 до 15, включая
            word = "".join(random.choices(letters, k=len_string))  # слово(строка) из списка letters с длиной
            # len_string
            list_string.append(word)  # Добавляем наше слово в список list_string
        result = " ".join(list_string)
        yield result  # Возвращаем результат и приостанавлием генератор


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
