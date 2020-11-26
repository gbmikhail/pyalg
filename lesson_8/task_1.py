# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
#
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9


def substring_values(text):
    # Для обеспечения уникальности, буду использовать мнодества
    hash_set = set()

    length = len(text)
    for c in range(1, length):               # Сколько
        for i in range(length - c + 1):      # Откуда
            sub_str = text[i:i + c]
            hash_set.add(hash(sub_str))
            # print(sub_str)

    return len(hash_set)


t1 = 'abcd'
t2 = 'papa'
t3 = 'sova'
print(t1, '->', substring_values(t1))
print(t2, '->', substring_values(t2))
print(t3, '->', substring_values(t3))
