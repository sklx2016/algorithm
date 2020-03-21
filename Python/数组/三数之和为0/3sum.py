# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2020/3/21 23:45
=================================================='''

def sum3(nums):
    n = len(nums)
    res = []
    if (not nums or n < 3 ):
        return  res
    nums.sort()
    for i in range(n):
        if (nums[i] > 0):
            return res
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        l = i + 1
        r = n - 1
        while(l < r):
            if (nums[i] + nums[l] + nums[r] == 0):
                res.append([nums[i], nums[l], nums[r]])
                while(l < r and nums[l] == nums[l + 1]):
                    l += 1
                while(l < r and nums[r] == nums[r - 1]):
                    r -= 1
                l += 1
                r -= 1
            elif (nums[i] + nums[l] + nums[j] > 0):
                r -= 1
            else:
                l += 1
    return res
