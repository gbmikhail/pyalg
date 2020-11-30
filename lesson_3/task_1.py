# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99

count = [0] * 8

for i in range(MIN_ITEM, MAX_ITEM + 1):
    for idx, j in enumerate(range(2, 10)):
        if i % j == 0:
            count[idx] += 1

for idx, i in enumerate(count, 2):
    print(f'{idx} - {i}')
