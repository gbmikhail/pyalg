# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

idx_min, idx_max = 0, 0
for idx, i in enumerate(arr):
    if i < arr[idx_min]:
        idx_min = idx

    if i > arr[idx_max]:
        idx_max = idx

print(arr)
print(f'min = {arr[idx_min]}\nmax = {arr[idx_max]}')
arr[idx_min], arr[idx_max] = arr[idx_max], arr[idx_min]
print(arr)
