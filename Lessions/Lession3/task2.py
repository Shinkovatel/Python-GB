# import modul
#
# # модульность
#
# print(modul.max1(5,9))
#
# from modul import max1 # импорт конкретного модуля, если * то импорт всех модулей
#
# print(max1(5,9))
#
# import modul as m1 # замена названия длинного модуля
#
# print(m1.max1(4,3))


# Рекурсия - функция которая вызывает сама себя.

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range (1, 10):
#     list_1.append(fib(i))
# print(list_1)

# алгоритмы

# быстрая сортировка

# def qwick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return qwick_sort(less) + [pivot] + qwick_sort(greater)
#
# print(qwick_sort([14,5,9,3,58,7,5,3,4,]))

# сортировка слияния

def merge_sorf(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sorf(left)
        merge_sorf(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k +=1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,2,3,5,6,32,3,24,74,84,9]

merge_sorf(list1)

print(list1)
