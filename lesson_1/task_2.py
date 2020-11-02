# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

_and = a & b
_or = a | b
_xor = a ^ b
ls = a << 2
rs = a >> 2

print(f"{a} = {bin(a)}")
print(f"{b} = {bin(b)}")

print(f"{a} & {b} = {bin(_and)}")
print(f"{a} | {b} = {bin(_or)}")
print(f"{a} ^ {b} = {bin(_xor)}")

print(f"{a} << 2 = {bin(ls)}")
print(f"{a} >> 2 = {bin(rs)}")
