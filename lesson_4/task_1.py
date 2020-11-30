# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Урок 3. Задача 4
# 4. Определить, какое число в массиве встречается чаще всего.
import cProfile
import random
import timeit

MIN_ITEM = 0
MAX_ITEM = 100


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

    return value, count


# Длину массива буду хранить в массиве. В моем случае: сделаю 5 замеров с шагом длины 100 - [100, 200, 300, 400, 500]
# Посчитал, что так будет проще и удобнее. Если получилось не хорошо - прошу понять и простить
# И результаты всего теста в таком случае, на мой взгляд смотряца лучше в конце. Надеюсь будет не критично.
size_list = [i for i in range(100, 500 + 1, 100)]
TEST_COUNT = 100

# **********************************************************************************************************************
print('*' * 40 + ' Вариант 1 ' + '*' * 40)
for idx, i in enumerate(size_list, 1):
    arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'{idx}. len = {i}\t', timeit.timeit('value, count = max_count_1(arr)', number=TEST_COUNT, globals=globals()))

# **********************************************************************************************************************
print('\n' + '*' * 40 + ' Вариант 2 ' + '*' * 40)
for idx, i in enumerate(size_list, 1):
    arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'{idx}. len = {i}\t', timeit.timeit('value, count = max_count_2(arr)', number=TEST_COUNT, globals=globals()))

# **********************************************************************************************************************
print('\n' + '*' * 40 + ' Вариант 3 ' + '*' * 40)
for idx, i in enumerate(size_list, 1):
    arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(i)]
    print(f'{idx}. len = {i}\t', timeit.timeit('value, count = max_count_3(arr)', number=TEST_COUNT, globals=globals()))


# cProfile. Длина списка: 5000
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(5000)]
# **********************************************************************************************************************
print('\n' + '*' * 28, "Вариант 1 cProfile: max_count_1 ", '*' * 28)
cProfile.run(f'max_count_1({arr})')

# **********************************************************************************************************************
print('*' * 28, "Вариант 2 cProfile: max_count_2 ", '*' * 28)
cProfile.run(f'max_count_2({arr})')

# **********************************************************************************************************************
print('*' * 28, "Вариант 3 cProfile: max_count_3 ", '*' * 28)
cProfile.run(f'max_count_3({arr})')

# РЕЗУЛЬТАТЫ:
# **************************************** Вариант 1 ****************************************
# 1. len = 100	 0.08407189999999999
# 2. len = 200	 0.3507544
# 3. len = 300	 0.8113667
# 4. len = 400	 1.5057317000000001
# 5. len = 500	 2.2821993999999997
#
# **************************************** Вариант 2 ****************************************
# 1. len = 100	 0.05165729999999957
# 2. len = 200	 0.18545320000000043
# 3. len = 300	 0.42380640000000014
# 4. len = 400	 0.7403975999999997
# 5. len = 500	 1.1710493
#
# **************************************** Вариант 3 ****************************************
# 1. len = 100	 0.002412899999999496
# 2. len = 200	 0.004443000000000197
# 3. len = 300	 0.006844300000000025
# 4. len = 400	 0.009112400000000243
# 5. len = 500	 0.01449519999999982
#
#
# **************************** Вариант 1 cProfile: max_count_1  ****************************
#          5 function calls in 2.557 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.548    2.548 <string>:1(<module>)
#         1    2.548    2.548    2.548    2.548 task_1.py:19(max_count_1)
#         1    0.009    0.009    2.557    2.557 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# **************************** Вариант 2 cProfile: max_count_2  ****************************
#          5 function calls in 1.286 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.277    1.277 <string>:1(<module>)
#         1    1.277    1.277    1.277    1.277 task_1.py:36(max_count_2)
#         1    0.009    0.009    1.286    1.286 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# **************************** Вариант 3 cProfile: max_count_3  ****************************
#          4 function calls in 0.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task_1.py:53(max_count_3)
#         1    0.012    0.012    0.014    0.014 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ВЫОД:
# Во всех 3-х вариантах наблюдается линейная зависимость.
# 1-й вариант: Перебирать весь список и сравнивать с каждым кначением - вариант мало эффективный
# 2-й вариант: Быстрее чем первый, т. к. количество сравниваемых значений с каждой уменьшается на 1
# 3-й вариант: Самый быстрый. Сравнивать со значением из словаря получается очень быстро,
#               так же список перебирается 1 раз
