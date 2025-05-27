# Задание 6.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
# в которой все гласные буквы заменены на символ '*'.



def replace_vowels(text):

    vowels = "ауеиоэяАУЕИОЭЯaeiouAEIOU"
    empty_string = ""

    for letter in text:
        if letter in vowels:
            empty_string += '*'
        else:
            empty_string += letter

    return empty_string

print("Замена гласных на символ '*'")

new_string = str(input("Введите текст: "))
result = replace_vowels(new_string)
print(f"Текст после замены: {result}")