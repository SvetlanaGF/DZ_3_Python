# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


print('Задача 3: Найти разницу между max и min значениями дробной части элементов списка.')
numbers_float = [1.1, 1.2, 3.1, 5.17, 10.02]
# numbers_float = [4.07, 5.1, 8.2444, 6.98]
count_num_float = len(numbers_float)

def fractional_part_calculation(minuend) -> float:
    """Выделяет дробную часть вещественного числа"""
    return minuend - int(minuend)

def min_calculation(minimum, number) -> float:
    """Определяет минимальное число"""
    if number < min:
        minimum = number
    return minimum

def max_calculation(maximum, number) -> float:
    """Определяет максимальное число"""
    if number > maximum:
        maximum = number
    return maximum

min = fractional_part_calculation(numbers_float[0])
max = fractional_part_calculation(numbers_float[1])

for i in range (0, count_num_float):
    fraction = fractional_part_calculation(numbers_float[i])
    min = min_calculation(min, fraction)
    max = max_calculation(max, fraction)

print(f'min =', round(min,4), 'max =', round(max,4))
print(f'Разница между max и min элементами =', round(max-min,4))