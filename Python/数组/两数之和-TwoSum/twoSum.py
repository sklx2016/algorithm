# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2020/11/22 17:14
=================================================='''
def twoSum(nums, target):
    map = dict()
    for i, num in enumerate(nums):
        if target - num in map:
            return [map[target - num], i]
        map[num] = i
    return []

print(twoSum([1, 2, 3, 4], 7))