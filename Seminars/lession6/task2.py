import random

my_list = [random.randint(0,9) for i in range(10)]
count = 0
print(my_list)
for i in range(1,len(my_list)-1):
    if my_list[i] > my_list[i-1] and my_list[i] > my_list[i+1]: # или if my_list[i]  < my_list[i-1] > my_list[i+1]:
        count += 1

print(count)

# по другому
my_list = [random.randint(0,9) for i in range(10)]
print(my_list)
print(len([i for i in range(1, len(my_list)-1) if my_list[i]  < my_list[i-1] > my_list[i+1]]))


