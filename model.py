# вычисления общего наименьшего знаменателя знаменателя
def lcm(num_1, num_2) -> int:
    i = max(num_1, num_2)
    # print(i)
    while ((i % num_1 != 0) or (i % num_2 != 0)):
        i += 1
    # print(i)
    return i

# Парсинг строки. (строка) -> (список)
def parsing(my_str):
    if "/" in my_str:
        new_list = my_str.split("/")
        new_list = [int(el) for el in new_list]
    else:
        new_list = [int(my_str), 1]
    return new_list

# вычисление
def calculate(num_1: list, num_2: list, op: str) -> list:
    numer1, denom1 = num_1
    numer2, denom2 = num_2
    nok = lcm(num_1[1], num_2[1])
    cf_1 = nok // num_1[1]
    cf_2 = nok // num_2[1]
    if op == '+':
        return [numer1 * cf_1 + numer2 * cf_2, nok]
    elif op == '-':
        return [numer1 * cf_1 - numer2 * cf_2, nok]
    elif op == '*':
        return [numer1 * numer2, denom1 * denom2]
    elif op == '/':
        return [numer1 * denom2, denom1 * numer2]

# def gen_list()

def rechange(lst_num) -> list:
    lst_num

