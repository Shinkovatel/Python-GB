
first_number = int(input('введите первое число: '))

difference = int(input('введите разность арифметической прогрессии: '))
count_numbers = int(input('введите количество членов арифметической прогрессии'))

my_list = []

for i in range(0,count_numbers):
    my_list.append(first_number + (i) * difference)

print(my_list)

