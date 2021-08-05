# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/7/23 17:51
@problem : 给定一个由若干 0 和 1 组成的数组 A ，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。
=================================================='''

def longestOnes(array, K):
    l, r, cnt0, res = 0, 0, 0, 0
    while l < r:
        if not array[r]:
            cnt0 += 1
            while cnt0 > K and l < r:
                if not array[l]:
                    cnt0 -= 1
                l += 1
        res = max(res, r - l + 1)
        r += 1
    return res

