# Задание 5.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
#       в которой все символы, которые не являются буквами, удалены (пробел разрешен).
#       Например: 'Hello, world!' -> 'Hello world'
#       Подсказка: используйте цикл и метод строки `isalpha()` для проверки, является ли символ буквой.



def remove_non_letters(text):

    empty_string = ""

    for letter in text:
        if letter.isalpha() or letter.isspace():
            empty_string += letter
    return empty_string

print("Удаление всех символов из строки(кроме букв)")

new_string = str(input("Введите строку для проверки: "))
result = remove_non_letters(new_string)
print(f"Результат: {result}")