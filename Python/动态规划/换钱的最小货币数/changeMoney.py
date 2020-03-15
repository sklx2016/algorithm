def changeMoney(array, aim):
    if len(array) == 0 or aim < 0:
        return -1
    n = len(array)
    max = 9999
    dp = [[0 for _ in range(aim + 1)] for _ in range(n)]
    for j in range(1, aim + 1):
        dp[0][j] = max
        if j - array[0] >= 0 and dp[0][j - array[0]] != max:
            dp[0][j] = dp[0][j - array[0]] + 1
    print(dp)
    left  = 0
    for i in range(1, n):
        for j in range(1, aim + 1):
            left = max
            if j - array[i] >= 0 and dp[i][j - array[i]] != max:
                left = dp[i][j - array[i]] + 1
            dp[i][j] = min(left, dp[i - 1][j])
    return dp[n - 1][aim] if dp[n - 1][aim] != max else -1


a = [1, 2, 3, 4, 5]
print(changeMoney(a, 10))






