def minPath(m):
    if len(m) == 0 or len(m[0]) == 0:
        return 0
    row = len(m)
    col = len(m[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = m[0][0]
    for i in range(1, row):
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for j in range(1, col):
        dp[0][j] = dp[0][j - 1] + m[0][j]
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
    return dp[row - 1][col - 1]

print(minPath([[1, 2, 3], [2, 3, 5], [1, 2, 3]]))



