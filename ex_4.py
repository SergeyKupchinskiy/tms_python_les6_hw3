# Задание 4.
# Напишите функцию, которая принимает на вход строку и возвращает True,
# если строка является палиндромом, и False - в противном случае.
#       Палиндром - это строка, которая читается одинаково в обоих направлениях.
#       Например: 'мадам', 'А роза упала на лапу Азора'



def is_palindrome(text):

    clean_text = ''.join(text.split()).lower()
    new_list = list(clean_text)
    reversed_list = new_list[::-1]
    return new_list == reversed_list

print("Проверка палиндромности")

new_string = str(input("Введите текст для проверки: "))
result = is_palindrome(new_string)
print(result)