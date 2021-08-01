'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

def findNumberIn2DArray(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    if len(matrix) == 0:
    	return false
    row = 0
    col = len(matrix[0])
    while row < len(matrix) && col >= 0:
    	if matrix[row][col] == target:
    		return true
    	elif matrix[row][col] > target:
    		col -= 1
    	else:
    		row += 1
    return false 

    