# Задание 3.
# Напишите функцию, которая принимает на вход строку и возвращает словарь,
# где ключи - это символы, а значения - количество этих символов в строке.
#       Например: 'Hello, world!' -> {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
#       Подсказка: используйте метод строки `count("a")`, который возвращает количество вхождений символа в строку.



def count_letters(text):

    new_dict = {}

    for letter in set(text):
        new_dict[letter] = text.count(letter)
    return new_dict

new_string = str(input("Введите текст: "))
result = count_letters(new_string)
print(f"Получаем словарь: {result}")