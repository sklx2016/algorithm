'''
leetcode 55
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
'''

# DP
def jumpGameDp(array):
    n = len(array)
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        if dp[i] != 1 : return False
        if i + array[i] >= n - 1 : return True
        for j in range(i + 1, i + array[i] + 1):
            dp[j] = 1

# Greedy
def jumpGameGreedy(array):
    n = len(array)
    maxLen = 0
    for i in range(n):
        if i > maxLen : return False
        maxLen = max(maxLen, i + array[i])
    return maxLen >= n - 1

def jumpGame(array):
    if not array:
        return 0
    jump = 0
    cur = 0
    next = 0
    for i in range(len(array)):
        if cur < i:
            cur = next
            jump += 1
        next = max(next, array[i] + i)
    return jump




