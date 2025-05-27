# Задание 2.
# Напишите функцию, которая принимает на вход строку и заменяет в ней все множественные пробелы на одинарные.
#       Например: 'Hello,    world' -> 'Hello, world'


def replace_multiple_spaces(text):

    words = text.split()
    new_text = " ".join(words)
    return new_text

new_string = str(input("Введите предложение с множественными пробелами: "))
result = replace_multiple_spaces(new_string)
print(f"Предложение без множественных пробелов: {result}")