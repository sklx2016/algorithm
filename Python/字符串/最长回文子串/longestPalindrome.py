# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/1/23 21:31
=================================================='''


def longestPalindrome(s):
    size = len(s)
    if size < 2:
        return s
    dp = [[False] * size  for _ in range(size)]
    max_len = 1
    start = 0

    for i in range(size):
        dp[i][i] = True

    for i in range(1, size):
        for j in range(0, i):
            if s[i] == s[j]:
                if i - j < 3:
                    dp[j][i] = True
                else:
                    dp[j][i] = dp[j + 1][i - 1]
            else:
                dp[j][i] = False
            if dp[j][i]:
                cur_len = i - j + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = j
    return s[start : start + max_len]

test = "axbbbbahxccccc"
print(longestPalindrome(test))

