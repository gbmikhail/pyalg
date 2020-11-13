# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код
# и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import cProfile
import timeit


def sieve(n):
    ls = list(range((n ** 2) + 3))
    ls[1] = 0
    for i in ls:
        if i > 1:
            for j in range(i + i, len(ls), i):
                ls[j] = 0

    index = 0
    for i in ls:
        if i > 0:
            index += 1
        if index == n:
            return i

    return None


def prime(n):
    assert n > 0, "Не верный индекс"
    index = 1
    value = 1
    while index <= n:
        value += 1
        for i in range(2, value):
            if value != i and value % i == 0:
                break
        else:
            index += 1

    return value


# # test
# print(prime(10))
# print(sieve(10))

TEST_COUNT = 100
size_list = [i for i in range(10, 100 + 1, 10)]

print('*' * 40 + ' prime ' + '*' * 40)
for idx, i in enumerate(size_list, 1):
    print(f'{idx:2}. prime({i})\t', timeit.timeit('prime(i)', number=TEST_COUNT, globals=globals()))
#  1. prime(10)	 0.0031156
#  2. prime(20)	 0.0104859
#  3. prime(30)	 0.027471199999999998
#  4. prime(40)	 0.0429217
#  5. prime(50)	 0.06922910000000002
#  6. prime(60)	 0.11100959999999999
#  7. prime(70)	 0.14479589999999998
#  8. prime(80)	 0.21153139999999998
#  9. prime(90)	 0.2441194000000001
# 10. prime(100)	 0.30581020000000003

print('\n' + '*' * 40 + ' sieve ' + '*' * 40)
for idx, i in enumerate(size_list, 1):
    print(f'{idx:2}. sieve({i})\t', timeit.timeit('sieve(i)', number=TEST_COUNT, globals=globals()))
#  1. sieve(10)	 0.002920899999999893
#  2. sieve(20)	 0.011708700000000016
#  3. sieve(30)	 0.026353700000000035
#  4. sieve(40)	 0.04688619999999988
#  5. sieve(50)	 0.0737791000000001
#  6. sieve(60)	 0.10606250000000017
#  7. sieve(70)	 0.14594470000000004
#  8. sieve(80)	 0.19489059999999991
#  9. sieve(90)	 0.24787939999999997
# 10. sieve(100)	 0.3088367000000001

# Одинаково работают
