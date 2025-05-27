# Задание 10.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку, в которой все символы,
# которые встречаются более одного раза, заменены на символ '_'.


def replace_duplicates(text):

    empty_dict = {}

    for letter in text:
        empty_dict[letter] = empty_dict.get(letter, 0) + 1

    symbol_replacement = ''.join('_' if empty_dict[letter] > 1 else letter for letter in text)

    return symbol_replacement

print("Замена дубликатов символов")

new_string = str(input("Введите текст для проверки: "))
result = replace_duplicates(new_string)
print(f"Результат: {result}")