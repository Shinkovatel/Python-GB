import random

number = int(input('введите число от 0 до 10: '))
array = [random.randint(0, 10) for i in range(10)]
find_number = 0;
array.sort()
print(array)
#number = int(input('введите число от 0 до 10: '))

for i in range(0, len(array)):
    if number >= array[i]:
        find_number = array[i]
print(f'ближашее к введенному числу {find_number}')