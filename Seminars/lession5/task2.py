def prime_numbers (n, div):
    if div == n // 2 + 1:
        print(f'yes, {div}') # правильно return "no"
    elif n % div == 0:
        print(f'no, {div} ')
    else:
        prime_numbers(n, div + 1)

value = int(input('введите число: '))
prime_numbers(value, 2)


def is_simple (num: int) -> bool: # анатация типов, что вернется
    if num in [1,2]:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range (3, num // 2+1, 2): # третий  аргумент, это шаг
            if num % i == 0
                return False

    return True

num = int(input('Введите число '))
print(f'число {num}' + ('простое' if is_simple(num) else 'составное'))
