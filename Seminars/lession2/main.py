#number = int(input('введите предел :'))

#fact = 1
#i = 1

# while i <= number:
  #  fact *= i
   # i += 1

#for i in range(1, number+1):
   # fact *= i

#print(fact)


#number_fib = int(input('введите n, которое вы хотите проверить: '))
#i = 1
#fibinachi_number1 = 0
#fibinachi_number2 = 1
#corent_fibonachi = 0
#while fibinachi_number2 < number_fib:
    #corent_fibonachi = fibinachi_number1 + fibinachi_number2
    #fibinachi_number2 = fibinachi_number1
    #fibinachi_number1 = corent_fibonachi
   # i += 1
    # алтернатива записи
 #   fibinachi_number1, fibinachi_number2 = fibinachi_number2, fibinachi_number1 + fibinachi_number2
  #  i += 1
#print(i if fibinachi_number2 == number_fib else -1)
    #print(corent_fibonachi)
    #if i == corent_fibonachi:
#print(i-1)
import random
#today = 0
#today += random.randint (-3,3) # возвращает рандомное число включая верную и нижнюю границу

#count_day = int(input('введите количество дней: '))
#i = 0
#count = 0
#max = 0
#while i <= count_day:
#    today += random.randint(-3, 3)
 #   print(today, end= " ")
#    if today > 0:
#        count += 1
#        if count > max:
#            max = count
 #   else:
       #count = 0
   #    i += 1
#print(f"\n\n{max}")

count_watermelon = int(input('введите количество арбузов :'))

#max = 1
#min = 30000

#for i in range(count_watermelon):
 #   result_watermelon = random.randint(1, 25000)
  #  print(f'вес арбуза {i+1} : {result_watermelon}')
  #  if result_watermelon > max:
#        max = result_watermelon
 #   if result_watermelon < min:
#        min = result_watermelon
#print(f'максимальный вес {max}, минимальный {min}')

# альтернатива через массив

watermelon = []

for i in range(0,count_watermelon):
    watermelon.append(random.randint(1,12))
max_weight = watermelon[0]
min_weight = watermelon[0]

for i in range(1, count_watermelon):
    if watermelon[i] > max_weight:
        max_weight = watermelon[i]
    if watermelon[i] < min_weight:
        min_weight = watermelon[i]
print(watermelon)
print(f'самый тяжелый {max_weight}, а самый легкий {min_weight}')
