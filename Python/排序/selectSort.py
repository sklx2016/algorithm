import random
#选择排序

def selectSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

A = [random.randint(1, 10) for i in range(10)]
print(selectSort(A))


