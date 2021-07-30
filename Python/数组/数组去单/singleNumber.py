# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/7/30 21:00
=================================================='''

'''
数组中所有数字出现两次，只有一个出现一次，求出它
连续异或
'''

def singleNumber(array):
    res = 0
    for i in range(len(array)):
        res = res ^ array[i]
    return res
