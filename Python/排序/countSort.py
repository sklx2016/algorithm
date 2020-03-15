# coding=UTF-8
#计数排序


import random
def countSort(array):
    length = max(array)
    count_array = [0] * (length + 1)
    for i in range(len(array)):
        count_array[array[i]] += 1
    index = 0
    for i in range(len(count_array)):
        if count_array[i] > 0:
            for j in range(count_array[i]):
                array[index] = i
                index += 1
    return array

A = [random.randint(0, 10) for i in range(20)]
print(A)
print(countSort(A))




