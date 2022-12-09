'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k(до 6 степени).*

        *Пример:*

        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

from random import randint

max_val = 100
k = int(input('Введите натуральную степень k: '))

koef = [randint(0, max_val) for i in range(k)] + [randint(1, max_val)]
equation = ' + '.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(koef) if j][::-1])
equation = equation.replace('x^1 +', 'x +')
equation = equation.replace('x^0', '')
equation += ('', '1')[equation[-1] == '+']
equation = (equation, equation[:-2])[equation[-2:] == '^1']
equation += " = 0"
print(equation)

with open('file_2.txt', 'w') as file:
    file.write(equation)
