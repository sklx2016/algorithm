# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/8/4 21:24
=================================================='''

'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

def movingCount(threshold, rows, cols):
    visited = [0] * (rows * cols)
    return movingCountCore(threshold, rows, cols, 0, 0, visited)

def movingCountCore(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row * cols + col] = 1
        count = 1 + movingCount(threshold, rows, cols, row, col, visited) + \
                    movingCount(threshold, rows, cols, row, col, visited) + \
                    movingCount(threshold, rows, cols, row, col, visited) + \
                    movingCount(threshold, rows, cols, row, col, visited)
    return count
def check(threshold, rows, cols, row, col, visited):
    if row >= 0 and row < rows and col >= 0 and col < cols and getDigitSum(row) + getDigitSum(col) <= threshold and \
            not visited[row * cols + col]:
        return True
    return False

def getDigitSum(number):
    sum = 0
    while number > 0:
        sum += (number % 10)
        number = number // 10
    return sum