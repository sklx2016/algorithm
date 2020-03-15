#矩阵路径数
def uniquePathI(m, n):
    if m <= 0 or n <= 0:
        return 0
    res= [0 for _ in range(n)]
    res[0] = 1
    for i in range(m):
        for j in range(n):
            res[j] += res[j - 1]
    return res[n - 1]


#矩阵路径数（路径中有障碍）
def uniquePathII(Grid):
    m, n = len(Grid), len(Grid[0])
    res = [1] + [0] * (n - 1)
    for i in range(m):
        for j in range(n):
            if Grid[i][j] > 0:
                res[j] = 0
            elif j > 0:
                res[j] += res[j - 1]
    return res[n - 1]

