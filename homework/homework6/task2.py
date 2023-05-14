import random
def filling_list(number):
    return [random.randint(0,20) for i in range(number)]

length = int(input('введите длину массива: '))
my_list = filling_list(length)
print(my_list)
min_number = int(input('введите минимальное число: '))
max_number = int(input('введите максимальное число: '))
new_list = []
for i in range(0,len(my_list)):
    if my_list[i] >= min_number and my_list[i] <= max_number:
        new_list.append(my_list[i])

print(new_list)



