# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 25
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

count = 0
value = 0
# Это, наверное, самое эффективное по скорости решение до которого я смог додуматься
length = len(arr)
for idx, x in enumerate(arr):
    tmp_count = 1
    for idy in range(idx + 1, length):
        if x == arr[idy]:
            tmp_count += 1

    if tmp_count > count:
        count = tmp_count
        value = x

print(arr)
if count < 2:
    print('Нет повторяющихся элементов')
else:
    print(f'Число {value} встречается {count} раз(а)')
