def print_sequence(n: int, s = '') -> str:
    ''' функция возвращает строчное значение от заданного числа до 1
    :param int
    :param str
    '''
    if n!= 0:
        s = s + str(n) + ' '
        return print_sequence(n-1, s)
    else:
        return s

n = int(input(' введите N :'))

num = int(input(' введите N :'))

print(print_sequence(n))
def revers (n: int):
    if n == 1:
        return n
    else:
        return f'{n} {revers(n-1)}'

print(revers(num))


if __name__ == "__main__":
    help(print_sequence)