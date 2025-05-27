# Задание 1.
# Напишите функцию, которая принимает на вход строку (предложение), а возвращает самое длинное слово из строки.

def longest_word(text):

    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

new_text = str(input("Введите предложение: "))
result = longest_word(new_text)
print(f"Саммое длинное слово в предложении: {result}")