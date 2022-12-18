# 3 - Дан массив размера N.
# После каждого отрицательного элемента массива
# вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

print('Задача: в заданном массиве вставить 0 после каждого отрицательного элемента:')
array = [-28, 46, -18, 19, 15, 11]
len_array = int(len(array))
array_index_negativ = []
print(f'Исходный массив:      ', array)

for i in range(len_array):
    if array[i] < 0:
        array_index_negativ.append(i)
    else:
        array_index_negativ.append('|')
print(array_index_negativ)

i = len_array

for i in range(len_array,0,-1):
    # print(i, array_index_negativ[i-1])
    if array_index_negativ[i-1] != '|':
        array.insert(i,0)
        # print(i, array_index_negativ[i-1])


print(f'Результирующий массив:', array)