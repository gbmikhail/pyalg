# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

f = int(input("Какую цифру вы хотите найти?: "))
n = int(input("Какое количество чисел вы будите вводить?: "))

count = 0
for i in range(n):
    a = int(input(f"Введите циру №{i + 1}: "))
    while a > 0:
        if a % 10 == f:
            count += 1
        a = a // 10

print(f"Среди {n} чисел, которые вы ввели, цифра {f} встречается {count} раз(а)")
