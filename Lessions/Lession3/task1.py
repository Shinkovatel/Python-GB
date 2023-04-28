
def sum_numbers(n, y = 'hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print('stop')
a = sum_numbers(5,'qwert')
print(a)

def sum_srt(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_srt('q','w','e'))

print()

