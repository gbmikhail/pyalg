# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр


def digit_sum(n):
    d = n % 10
    n = n // 10
    if n > 0:
        return d + digit_sum(n)
    return d


max_n = max_s = 0
while True:
    n = int(input('Введите число: '))
    if n == 0:
        break
    s = digit_sum(n)
    if s > max_s:
        max_s, max_n = s, n

print(f'Наибольшее число по сумме цифр: {max_n}. Сумма цифр: {max_s}')
