# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input("Введите номер буквы в алфавите (a-z). Нумерация с единицы: "))

ch_pos = ord('a') + n - 1
ch = chr(ch_pos)
print(f"Это буква: {ch}")
