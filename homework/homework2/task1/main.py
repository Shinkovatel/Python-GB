import random

coin = int(input('введите количество монет: '))

coins = []

for i in range(0,coin):
    coins.append(random.randint(0,1))
print(coins)

if coins.count(1) > coins.count(0):
    print(f'переворачиваем решки, их меньше чем орлов {coins.count(0)}')
elif coins.count(1) == coins.count(0) :
    print(f'равное количество неважно что переворачивать {coins.count(1)}')
else:
    print(f'переворачиваем орлы, их меньше чем решек {coins.count(1)}')


# альтернативный вариант заполнения массива
count_zero = 0
count_one = 0

for i in range(coin):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
