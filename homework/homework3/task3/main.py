#
import re
text = input('введите слово: ').upper()
#text1 = (text)
print(text)

#
dict = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}
# dictionary1 = {
#      ** dict.fromkeys(['a','e','i','o','l','n','s','t','r'],1),
#      ** dict.fromkeys(['d','g'],2),
#      ** dict.fromkeys(['b','c','m','p','f','h','v','w','y'],3)
# }

sum = 0

for i in text:
    for k,v in dict.items():
        if i in v:
            sum += k


print(sum)

# другой вариант найденный в сети
# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))