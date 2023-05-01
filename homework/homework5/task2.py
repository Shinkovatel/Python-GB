
def summ (numA: int, numB: int):
    ''' функция возвращает число'''
    if numA == 0: return numB
    else:
        return summ(numA-1,numB +1)

numberA = int(input('введите число A: '))
numberB = int(input('введите число B: '))

print(f'{summ(numberA,numberB)}')

