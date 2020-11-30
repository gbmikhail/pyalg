# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index = -1
for idx, i in enumerate(arr):
    if i < 0 and index < 0:
        index = idx
    elif (i < 0) and (i > arr[index]):
        index = idx

print(arr)

if index < 0:
    print('Нет отрицательных элементов')
else:
    print(f'В массиве максимальный отрицательный элемент: {arr[index]}. Его позиция: {index}')
