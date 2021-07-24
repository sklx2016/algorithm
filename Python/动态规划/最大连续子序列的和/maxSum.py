# -*- coding: utf-8 -*-
# @Author: skkkkkk
# @Date:   2021-07-24 23:30:42
# @Last Modified by:   skkkkkk
# @Last Modified time: 2021-07-24 23:54:58

'''
求子序列的和最大值
eg. [1, 2, 3, -7, 1, 2]  最大值为 1+2=3
'''

def maxSum(array):
	thisSum, res = 0, 0
	for i in range(len(array)):
		thisSum += array[i]
		if thisSum > res:
			res = thisSum
		elif thisSum < 0:
			thisSum = 0
	return res