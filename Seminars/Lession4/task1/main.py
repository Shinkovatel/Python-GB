# input_string = input('введете строку: ')
#
# chars = list(input_string) # без пробелов
# # иначе
#
# chars1 = input_string.split() # если есть пробелы.
#
# letter = dict()
#
# for i in chars:
#     if (i in letter):
#         letter[i] = letter[i] + 1
#
#     else:
#         letter[i] = 0
#     count_of_repeats = letter[i]
#     print(f"{i}_{count_of_repeats}" if count_of_repeats > 0 else i, end=' ') # end определяет как закачивается строка


# альтернативный вариант в вводом через пробел

str = input('введете строку: ').split()
chars2 = {}

for i in str:
    if i in chars2:
        print(f"{i}_{chars2[i]}", end =' ')
    else:
        print(i, end='')
    chars2[i] = chars2.get(i,0)+ 1
print('\n')

# вариант препода

str = input('введете строку: ').split()
chars3 = {}

for letter in str:
    chars3[letter] = chars3.get(letter,0) + 1 # в процедуре get 0 нужен чтобы вернуть значение 0 иначе будет None, а его нельзя сложить
    print(letter if chars3.get(letter) == 1 else f'{letter}_{chars3.get(letter)-1}', end='')


