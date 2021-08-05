# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/8/5 17:00
=================================================='''

'''
给定两个整数数组 a 和 b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差。
'''

import sys
def smallestDifference(a, b):
    a.sort()
    b.sort()
    i, j, n, m, res = 0, 0, len(a), len(b), sys.maxsize
    while i <= n and j <= m:
        res = min(res, abs(a[i] - b[j]))
        if a[i] > b[j]:
            j += 1
        else:
            i += 1
    return res


