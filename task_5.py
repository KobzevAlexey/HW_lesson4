# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.*


def make_dict(equation):
    dict_equation = {}
    equation = equation.replace(' + ', ' +').replace(' - ', ' -').replace(' = 0', 'x^0')
    equation = equation.replace('x ', 'x^1 ')
    equation = equation.split()
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dict_equation[int(equation[i][1])] = int(equation[i][0])
    return dict_equation


def sum_equation(dict_equation_1, dict_equation_2):
    dict_res = {}
    max_eq = (max(max(dict_equation_1), max(dict_equation_2)))
    for i in range(max_eq, -1, -1):
        first = dict_equation_1.get(i)
        second = dict_equation_2.get(i)
        if first is not None or second is not None:
            dict_res[i] = (first if first is not None else 0) + (second if second is not None else 0)
    return dict_res


def final_equation(dict_res):
    result = ''
    for i in dict_res.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^1', 'x').replace('x^0', ' = 0')
    return result


with open('file_1.txt') as data:
    equation_1 = data.readline()
with open('file_2.txt') as data:
    equation_2 = data.readline()

dict_equation_1 = make_dict(equation_1)
dict_equation_2 = make_dict(equation_2)
dict_result = sum_equation(dict_equation_1, dict_equation_2)
final = final_equation(dict_result)
with open('file_fin.txt', 'w') as file:
    file.write(final)
