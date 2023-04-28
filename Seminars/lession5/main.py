def fibo (n):
    if n in [0,1]:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input('Enter a number'))

print((f'element {n} of fibo {fibo(n)}'))

def func(n):
    if n==0:
        return 1
    return func(n+1)


import random

marks = [random.randint(1,5) for _ in range(10)]

print(marks)

max_marks = max(marks)
min_marks = min(marks)
print(max_marks)

for i in range(len(marks)):
    if marks[i] == max_marks: marks[i] = min_marks

print(marks)


