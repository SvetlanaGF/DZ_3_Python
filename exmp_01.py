# 1- Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Задача 1: Из списка чисел найти сумму нечетных элементов списка.')
numbers = [2, 3, 5, 9, 3]

def sum_odd_num(number):
    """Находит сумму элементов на нечетных позициях списка"""
    count_num = len(number)
    sum = 0
    print('Элементы на нечетных позициях в списке:')
    for i in range(1,count_num,2):
        print(number[i])
        sum += number[i]
    return sum

result = sum_odd_num(numbers)
print(f'Сумма нечетных элементов =', result)