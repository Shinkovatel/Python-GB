def f(x):
    return x*x

a = f # хранит в себе ссылку на функцию
print(a(5))
print(f(5))

def calc1(a, b):
    return a+b

def calc2(a, b):
    return a*b

def math(op,x, y):
    print(op(x,y))

math(calc1, 5, 6)

# лямба фунция для сокращения

calc1 = lambda a,b: a + b # сокращенная запись функции def calc1

# упрощенная запись

math(lambda a,b: a+b, 56, 4)


data = [1,2,3,5,8,15,23,38]

res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)

# def select(f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

res1 = map(int, data)

res1 = filter(lambda x: x%2 ==0, res1)

res1 = list(map(lambda x: (x, x**2), res1))

list2 = [x for x in range(1,20)]
print(list2)

list2 = list(map(lambda x: x+10, list2))

print(list2)


data_1 = '12 1234 123 54 64 6456'
print(data_1)
# data_1 = data_1.split()
# print(data_1)

data_1 = list(map(int, data_1.split()))

print(data_1)

# filter (на вход принимает 2 аргумента(функция и объект)  возвращает только элементы объекта для которых вызов функции которую мы передали вернула значение True)

data_2 = [15,65,2,325,44]

res = list(filter(lambda x: x % 10 == 5, data_2))

# функция Zip применияется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

# на вход подается 3 списка, в результате берется первый элемент из первого списка, первый элемент из второго списка и 1 элпемент из 3-го списка и т. д.


users = ['user1', 'user2', 'user3']
ids = [4,5,6]

data_3 = list(zip(users, ids))

print(data_3)

users1 = ['user1', 'user2', 'user3']
ids1 = [4,5,6]
salary = [111,222,333]

data_4 = list(zip(users1,ids1,salary))
print(data_4)

# Enumerate - применяется к итеруруемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных, позволяет пронумеровать набор данных

sity = ['Казань', 'Астрахань', 'Смоленск']

data_5 = list(enumerate(sity))

print(data_5)


# работа с файлами

# a - открытие для добавления данных (дописываение, создание нового)
# r - читает данные из только из существующего файла
# w - запись данных и создание файла
# w+ - Открытие файла для записи и чтения из него
# r+ - Открытие и дописывание в него


colors = ['red', 'blue', 'green']
data_6 = open('file.txt', 'a')
data_6.writelines(colors) # пишется подряд
data_6.close()


with open('file.txt', 'a') as data_6:
    data_6.write('line 1\n')
    data_6.write('line 2\n')

print(56)

# режис чтения

path = 'file.txt'
data_6 = open('file.txt','r')
for line in data_6:
    print(line)
data_6.close()
