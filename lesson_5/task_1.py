# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

counter = Counter()

n = int(input('Введите количество организаций: '))
for i in range(n):
    name = input(f'Введите название организации №{i + 1}: ')
    counter[name] = 0
    for k in range(4):
        counter[name] += int(input(f'Введите прибыль за {k + 1}-й квартал: '))

avg = sum(counter.values()) / len(counter.values())
print('Средняя прибыль всех компаний', avg)

print('\nКомпании с прибылью выше среднего: ')
for i in counter:
    if counter[i] > avg:
        print(f'{i:25}', counter[i])

print('\nКомпании с прибылью ниже среднего (и среднего): ')
for i in counter:
    if counter[i] <= avg:
        print(f'{i:25}', counter[i])
