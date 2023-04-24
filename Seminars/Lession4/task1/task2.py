import string

str = input('введете строку: ').replace('.', ' ').lower().split() # replace нужно для того чтобы заменить некоторые символы lower() - перевод в нижний регистр

str1 = input('введете строку: ')

my_str = set(str)

for i in string.punctuation: # отчистка от пунктуации
    str1 = str1.replace(i, ' ')

print(my_str)
print(len(my_str))

print(string.digits)
print(string.printable)
print(string.ascii_letters)
print(string.hexdigits)