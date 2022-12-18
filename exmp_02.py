# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

print('Задача 2: Найти произведение пар чисел списка (первый и последний и т.д.).')
# numbers = [2, 3, 4, 5, 6]
numbers = [2, 3, 5, 6]
count_num = len(numbers)
multiplication = 1
result = []
count = 1

count_pair = len(numbers) // 2

def output_pair(element, first, second):
    """Выводит на консоль пару перемножаемых чисел"""
    print(f'Пара', element+1, ':', first, '-', second)

def product_calcilation(multiplicanda, multiplier):
    """Возвращает произведение двух чисел"""
    return multiplicanda * multiplier

def counter(second_in_a_pair):
    """Возвращает индекс второго элемента в паре"""
    return second_in_a_pair + 1

for i in range(0,count_pair+1):
    if i != count_pair:
        output_pair(i, numbers[i], numbers[count_num - count])
        multiplication = product_calcilation(numbers[i], numbers[count_num - count])
        result.append(multiplication)
    else:
        if count_num % 2 != 0:
            output_pair(i, numbers[i], numbers[i])
            multiplication = product_calcilation(numbers[i], numbers[i])
            result.append(multiplication)

    count = counter(count)
    
print(f'Результат:', result)