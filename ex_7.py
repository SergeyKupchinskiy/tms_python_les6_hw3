# Задание 7.
# Напишите функцию, которая принимает на вход число и возвращает сумму его цифр.


def sum_digits(number):

    digits = str(number)
    digits_sum = sum(int(digit) for digit in digits)
    return digits_sum

print("Найти сумму цифр у числа")

new_number = int(input('Введите число: '))
result = sum_digits(new_number)
print(f"Результат: {result}")