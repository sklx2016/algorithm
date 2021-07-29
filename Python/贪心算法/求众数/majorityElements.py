# -*- coding: utf-8 -*-
# @Author: skkkkkk
# @Date:   2021-07-25 22:31:54
# @Last Modified by:   skkkkkk
# @Last Modified time: 2021-07-26 00:12:25
'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 n/2 的元素

摩尔投票法：每次删除两个不同的数，剩下的就是出现次数最大的数


如果存在某个数超过 1/3 ，那我们每次删掉三个不同的数，直到最后没法删，最后剩下的数一定有这个超过 1/3 的数。
原因很简单，因为每删一次最多删掉一个这个数，而删除最多 1/3 数组长度次之后所有数都被删光了，但是这个数还剩下一点。

'''

def majorityElements(array):
	res, cnt = 0, 0
	for num in array:
		if cnt == 0:
			res = num 
			cnt = 1
		elif num == res:
			cnt += 1
		else:
			cnt -= 1





