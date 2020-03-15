#插入排序
import random

def insertSort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[j] >= array[i]:
                array.insert(j, array[i])
                array.pop(i + 1)
                break
    return array

A = [random.randint(1, 10) for i in range(10)]
print(A)
A.insert(1, 0)
print(A)
print(insertSort(A))




