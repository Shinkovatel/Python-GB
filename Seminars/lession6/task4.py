

def divid (number: int) -> list:
    return [i for i in range(1, number//2 +1) if number % i == 0]

#checked = set()
for i in range(1,10000):
    sum_i_dividers = sum(divid(i))
    for j in range(i+1,10001):
        if(j == sum_i_dividers and i == sum(divid(j))): # оператор И работает так: если первое правда проверяет второе, если первое не правда, второе не проверяет
            print(f'{i} {j}')


# альтернативный вариант

import math

def sum_of_divisors(n):
    sum = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            sum += i
            if i != n/i:
                sum += n/i

    return sum

k = int(input())

for i in range(1, k+1):
    sum1 = sum_of_divisors(i)
    if sum1 <= k:
        sum2 = sum_of_divisors(sum1)
        if sum2 == i and i < sum1:
            print(i,sum1)

# вариант препода
def sum_dividers (number1):
    sum_div = 0
    for div in range(1, number1 // + 1 ):
        if not number1 % div:
            sum_div += div

    return sum_div

all_numbers = {number1: sum_dividers(number1) for number1 in range(10000)}

for num in range(10000):
    if num == all_numbers.get(all_numbers.get(num)) and num < all_numbers.get(num): # после И убирает повторные условия
        print(num, sum_dividers(num), sep=' \U0001F91D ')