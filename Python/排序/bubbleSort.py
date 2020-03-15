#冒泡排序
import random

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

A = [random.randint(1, 10) for i in range(10)]
print(bubbleSort(A))




