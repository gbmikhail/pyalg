# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


class Column:
    # Будет универсальна, с базой. Иначе 16 придется везде писать - не практично
    def __init__(self, str_value='0', base=16):
        self.digits = deque(str_value.lower())
        self.BASE = base
        self.DEC_TO_HEX_DICT = {i: str(i) if i < 10 else chr(ord('a') + (i - 10)) for i in range(0, base)}
        self.HEX_TO_DEC_DICT = {str(i) if i < 10 else chr(ord('a') + (i - 10)): i for i in range(0, base)}

    def __str__(self):
        # return '0x' + ''.join(self.digits)
        return ''.join(self.digits)

    def __add__(self, other):
        assert self.BASE == other.BASE, "Системы счисления должны совпадать"
        max_len = max(len(self.digits), len(other.digits))
        res_value = deque()
        mem = 0
        for idx in range(1, max_len + 1):
            v1 = self.digits[-idx] if len(self.digits) >= idx else '0'
            v2 = other.digits[-idx] if len(other.digits) >= idx else '0'

            cv = self.HEX_TO_DEC_DICT[v1] + self.HEX_TO_DEC_DICT[v2] + mem
            if cv >= self.BASE:
                cv -= self.BASE
                mem = 1
            else:
                mem = 0
            res_value.appendleft(str(self.DEC_TO_HEX_DICT[cv]))

        if mem > 0:
            res_value.appendleft(str(self.DEC_TO_HEX_DICT[mem]))

        return Column(''.join(res_value), base=self.BASE)

    def __mul__(self, other):
        assert self.BASE == other.BASE, "Системы счисления должны совпадать"
        sum_ls = deque()
        for idx in range(1, len(other.digits) + 1):
            row_value = deque()
            mem = 0
            for _ in range(idx - 1):
                row_value.appendleft('0')
            for idy in range(1, len(self.digits) + 1):
                a = self.digits[-idy]
                b = other.digits[-idx]
                cv = self.HEX_TO_DEC_DICT[a] * self.HEX_TO_DEC_DICT[b] + mem
                mem = cv // self.BASE
                cv = cv % self.BASE

                row_value.appendleft(str(self.DEC_TO_HEX_DICT[cv]))
            if mem > 0:
                row_value.appendleft(str(self.DEC_TO_HEX_DICT[mem]))
            sum_ls.append(row_value)

        res_value = Column(base=self.BASE)
        for i in sum_ls:
            vl = ''.join(i)
            res_value += Column(vl, base=self.BASE)

        return res_value


a = Column('a2')
b = Column('c4f')
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')

a = Column('1fe')
b = Column('8a79')
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
