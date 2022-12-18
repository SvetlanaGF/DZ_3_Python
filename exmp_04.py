# 4- Напишите программу,
# которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример: 45 -> 101101    3 -> 11     2 -> 10

print('Задача 4: Преобразовать десятичное число в двоичное.')
print('Использовать рекурсию, не использовать функцию bin.')
dividend = int(input('Введите число '))

def conversion (dividend) -> str:
    if dividend < 2:
        """Выводит в двоичной системе числа 0 и 1"""
        print(dividend) 
        return str(dividend)
    else:
        """Выводит в двоичной системе числа больше 1"""
        remainder = dividend % 2
        dividend = dividend // 2
        return conversion(dividend) + str(remainder)

res = conversion(dividend)
print(res)

print(f'Десятичное число ->', dividend, 'в двоичной системе ->', res)
