def LCS(s1, s2):
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    max_num = 0
    res = ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    max_num = dp[len(s1)][len(s2)]
    #打印出相同的子序列
    n = len(s1)
    m = len(s2)
    while max_num > 0:
        if n > 0 and m > 0:
            if dp[n][m] == dp[n - 1][m]:
                n -= 1
            elif dp[n][m] == dp[n][m - 1]:
                m -= 1
            else:
                res += s1[n - 1]
                n -= 1
                m -= 1
                max_num -= 1
    print(res[::-1], dp[len(s1)][len(s2)])

LCS('asdfgtr', 'asbnmcdfgt')








