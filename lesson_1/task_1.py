# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите трехзначное число: "))

s = a % 10
p = a % 10
a = a // 10

s += a % 10
p *= a % 10
a = a // 10

s += a % 10
p *= a % 10
a = a // 10

print(f"Сумма цифр : {s}")
print(f"Произведение цифр : {p}")
