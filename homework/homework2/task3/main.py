number = int(input('введите число'))
count = 0
result_a = [2**i for i in range(number)]
result_b = []
for i in range(number):
    if result_a[i] < number:
       count +=1
result_b = [count]
for i in range(number):
    if result_a[i] < number:
        result_b[i] = result_b.append(i)
    #elif result_a[i] > number:
print(result_b)
#print(result)
# Решение основное...

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1