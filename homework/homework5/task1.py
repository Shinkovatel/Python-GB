def my_degree (number: int, degree: int) -> int:
    if degree == 0: return 1
    elif degree == 1: return number
    return number * my_degree(number, degree-1)

my_number = int(input('введите число: '))
degree = int(input('введите степень числа: '))

print(f'число {my_number} возведенное в степень {degree} равно {my_degree(my_number,degree)}')

