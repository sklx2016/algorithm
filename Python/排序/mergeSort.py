# -*- coding:utf-8 -*-
#归并排序
import random

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        mid = int(len(array) / 2)
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
        return merge(left, right)

test = [random.randint(1, 50) for i in range(10)]
print(mergeSort(test))


