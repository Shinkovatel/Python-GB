import random

number = int(input('введите число от 0 до 10: '))
array = [random.randint(0, 10) for i in range(10)]
count = 0
print(array)
for i in range(0, len(array)):
    if array[i] == number:
        count += 1
    # else:
    #    break
print(f'количество совпадающих чисел {count}')

