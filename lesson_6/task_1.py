# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Выбрана задача из Урок 3. Задача 4
# 4. Определить, какое число в массиве встречается чаще всего.

import random
import sys


def var_size(x):
    size = sys.getsizeof(x)
    # print(f'type(x)={type(x)}, sys.getsizeof(x)={size},x={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += var_size(key)
                size += var_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += var_size(item)
    return size


def max_count_1(ar):
    count = 0
    value = 0
    length = len(ar)
    for x in ar:
        tmp_count = 0
        for idy in range(length):
            if x == ar[idy]:
                tmp_count += 1

        if tmp_count > count:
            count = tmp_count
            value = x

    # Считаем размер переменных
    print('*' * 40, 'max_count_1', '*' * 40)
    # ar - по идеи не относится к самой функции - передаем из вне. Поэтому игнорим, срезом из dir,
    # но можно if i == 'ar': continue в for
    var_list = dir()[1:]
    size = 0
    for idx, i in enumerate(var_list, 1):
        s = var_size(eval(i))
        print(f'{idx}. {i:20}{s} bytes')
        size += s
    print(f'Total: {size} bytes\n')

    return value, count


def max_count_2(ar):
    count = 0
    value = 0
    length = len(ar)
    for idx, x in enumerate(ar):
        tmp_count = 1
        for idy in range(idx + 1, length):
            if x == arr[idy]:
                tmp_count += 1

        if tmp_count > count:
            count = tmp_count
            value = x

    # Считаем размер переменных
    print('*' * 40, 'max_count_2', '*' * 40)
    # ar - по идеи не относится к самой функции - передаем из вне. Поэтому игнорим, срезом из dir,
    # но можно if i == 'ar': continue в for
    var_list = dir()[1:]
    size = 0
    for idx, i in enumerate(var_list, 1):
        s = var_size(eval(i))
        print(f'{idx}. {i:20}{s} bytes')
        size += s
    print(f'Total: {size} bytes\n')

    return value, count


def max_count_3(ar):
    count_dict = {}
    count = 0
    value = 0
    for i in ar:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

        if count_dict[i] > count:
            count = count_dict[i]
            value = i

    # Считаем размер переменных
    print('*' * 40, 'max_count_3', '*' * 40)
    # ar - по идеи не относится к самой функции - передаем из вне. Поэтому игнорим, срезом из dir,
    # но можно if i == 'ar': continue в for
    var_list = dir()[1:]
    size = 0
    for idx, i in enumerate(var_list, 1):
        s = var_size(eval(i))
        print(f'{idx}. {i:20}{s} bytes')
        size += s
    print(f'Total: {size} bytes\n')

    return value, count


MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 100

arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr, f'size = {var_size(arr)}', sep='\n')

value1, count1 = max_count_1(arr)
# print(value1, count1)

value2, count2 = max_count_2(arr)
# print(value2, count2)

value3, count3 = max_count_3(arr)
# print(value3, count3)


# ОС: Windows 10 x64
# Python: 3.6 x64

# РЕЗУЛЬТАТ РАБОТЫ
# [18, 47, 72, 95, 61, 52, 62, 19, 36, 84, 15, 67, 41, 31, 61, 91, 50, 0, 64, 77, 15, 64, 96, 93, 31, 0, 9, 5, 98, 50, 41, 62, 41, 11, 95, 76, 9, 11, 98, 54, 16, 3, 18, 17, 91, 13, 6, 47, 70, 76, 5, 25, 82, 55, 8, 26, 21, 51, 100, 55, 28, 4, 81, 22, 85, 91, 49, 21, 55, 44, 11, 37, 51, 93, 55, 81, 93, 79, 29, 3, 80, 32, 51, 17, 31, 64, 10, 75, 92, 94, 24, 80, 4, 31, 26, 76, 60, 43, 20, 2]
# size = 3704
# **************************************** max_count_1 ****************************************
# 1. count               28 bytes
# 2. idy                 28 bytes
# 3. length              28 bytes
# 4. tmp_count           28 bytes
# 5. value               28 bytes
# 6. x                   28 bytes
# Total: 168 bytes
#
# **************************************** max_count_2 ****************************************
# 1. count               28 bytes
# 2. idx                 28 bytes
# 3. idy                 28 bytes
# 4. length              28 bytes
# 5. tmp_count           28 bytes
# 6. value               28 bytes
# 7. x                   28 bytes
# Total: 196 bytes
#
# **************************************** max_count_3 ****************************************
# 1. count               28 bytes
# 2. count_dict          5748 bytes
# 3. i                   50 bytes
# 4. value               28 bytes
# Total: 5854 bytes

# ВЫВОД
# В варианте 1 использовались в циклы, памяти на перебор понадобилось минимальнойе количество - 168 байт (но медленно)
# Вариант 2 очень мохож на вариант 1 - те же цыклы, но количество переборов в цыкле меньше, для этогобыла задействована
#   дополнительная переменная idx (+28 байт по сравнению с первым). Итого получилось 196 байта.
#   По соотношению скорость/память он занимает более выигрышное положение по сравнению с первым (28 байт - я бы
#   пожертвовал ради прироста скорости ~ в 2 раза)
# Вариант № 3 самый затратный в плане памяти из-за использования словаря (5748 байт).
#   Всего в данном примере получилось 5854 байта и этот объем будет увеличиваться в случае увеличения размера
#   исходного массива и/или увеличения диапазона randint.
#   Но этот вариант получился наименее времязатратный
