# Вычислить число ПИ c заданной точностью d  - при d = 0.0001, π = 3.1415

import math


def fix(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0' * (n - len(b)))


d = str(input('Введите d: '))
count = abs(d.find('.') - len(d)) - 1
print(fix(math.pi, count))