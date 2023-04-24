import random
from collections import deque

quantity_array = int(input('введите количество кустов черники: '))
array = [random.randint(0, 20) for i in range(quantity_array)]
print(array)
summ = 0
count = 0
res = []
for i in range(0,len(array)-1):
    res.append(array[i]+array[i-1] + array[i+1])
res.append(array[-1]+array[-2] + array[0])
print(res)

for i in range(0, len(res)):
    if res[i] > summ:
        summ = res[i]
        count = i
print(f'максимальное количество ягод равное {summ} можно получить на грядке {count}')
print(summ)
