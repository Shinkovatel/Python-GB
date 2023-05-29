from itertools import zip_longest

# map - принимает функцию и ко всем элементам коллекциям

my_string = '1234567'
my_string = list(my_string)

for i in range(len(my_string)):
    my_string[i] = int(my_string[i])

#
my_string = list(map(int, my_string))

# использовали с лямбда функцией
my_string = list(map(lambda x: x + '1', my_string))

# filter - результат функции True пропускает если нет то нечего

my_string = list(filter(lambda x: x.isdigit(), my_string))


# enumerate - нумерация коллекции и вывод ввиде кортежа

for i, item in enumerate(my_string):
    print(i, item)

# zip - соединяет элементы попарно в кортеже если нет полного сопоставления то меньшего сопостовления
my_string1 = '12345545466'
my_string2 = 'xfsdfsdfsdf'
list_1 = list(my_string1)
list_2 = list(my_string2)

new_list = []
for i in enumerate(list_1):
    new_list.append(list_1[i],list_2[i])

new_list1 = list(zip(list_1, list_2))
new_list2 = list(zip_longest(list_1,list_2, fillvalue='Ничего')) # нужно всегда перевеодит в список, если нужно перебрать то можно использовать однократно

for i in zip_longest(list_1,list_2, fillvalue='Ничего'):
    print(i)


# lambda

def is_digit(num: str):
    return num.isdigit()

lambda x: x.isdigit() # можно передавать более одного аргумента



