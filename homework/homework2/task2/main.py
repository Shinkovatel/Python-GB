import math

summ = int(input('введите сумму чисел'))
qvad = int(input('введите произведение чисел'))

for search_a in range(summ):
    for search_b in range(qvad):
        if search_b + search_a == summ and search_b * search_a == qvad:
            print (search_b,search_a)
