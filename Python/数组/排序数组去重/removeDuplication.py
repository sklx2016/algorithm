# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/7/30 20:48
=================================================='''

def removeduplication(array):
    length = len(array)
    index = 0
    for i in range(1, length):
        if array[i] != array[index]:
            index += 1
            array[index] = array[i]
    return index + 1

