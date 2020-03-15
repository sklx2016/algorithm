# -*- coding:utf-8 -*-
#快速排序

import random

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        a = array[0]
        left = [i for i in array[1 : ] if i <= a]
        right = [i for i in  array[1 : ] if i > a]
        return quickSort(left) + [a] + quickSort(right)

test = [random.randint(1, 50) for i in range(10)]
print(quickSort(test))








'''
a = list(map(int, input().strip().split()))
n = a[0]
k = a[1]
array = list(map(int, input().strip().split()))
count_0 = 0
zero_index = []
for i in range(n):
    if array[i] == 0:
        count_0 += 1
        zero_index.append(i)
if k >= count_0:
    print(n)
else:
    end = k + 1
    res = 0
    for i in range(len(array)):
        if end < len(array):
            res = max(res, array[end] - array[i] - 1)
            end += 1
    c = len(array) - array[-k]
    d = array[k]
    res = max(res, c, d)
    print(res)
    
'''