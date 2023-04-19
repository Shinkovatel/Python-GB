# Alias = {
#     'a' : 'id1',
#     'e' : 'id1',
#     'i' : 'id1',
#     'o' : 'id1',
#     'l' : 'id1',
#     'n' : 'id1',
#     's' : 'id1',
#     't' : 'id1',
#     'r' : 'id1',
#     'd' : 'id2',
#     'g': 'id2',
#     'b': 'id3',
#     'c': 'id3',
#     'm': 'id3',
#     'p': 'id3',
#     'f': 'id3',
#     'h': 'id3',
#     'v': 'id3',
#     'w': 'id3',
#     'y': 'id3',
#
# }

text = input('введите слово: ')
text1 = list(text)
print(text1)

dictionary = {
     ** dict.fromkeys(['a','e','i','o','l','n','s','t','r'],1),
     ** dict.fromkeys(['d','g'],2),
     ** dict.fromkeys(['b','c','m','p','f','h','v','w','y'],3)
}

print(dictionary)
sum = 0
for i in range(0,len(text1)):
    if text1[i] == dictionary.keys():
        sum += dictionary.values()
print(sum)