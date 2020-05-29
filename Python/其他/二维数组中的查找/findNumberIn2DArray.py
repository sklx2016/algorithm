# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2020/5/29 17:17
=================================================='''

'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

def findNumberIn2DArray(arr, target):
  i = len(arr) - 1
  j = 0
  while (i >= 0 and j < len(arr[0])):
    if target < arr[i][j]:
      i -= 1
    elif target > arr[i][j]:
      j += 1
    else:
      return True
  return False

print(findNumberIn2DArray([[1, 2], [3, 4]], 2))
