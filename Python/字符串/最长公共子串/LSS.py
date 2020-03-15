def LSS(s1, s2):
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    max_num = 0
    index = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > max_num:
                    max_num = dp[i + 1][j + 1]
                    index = i + 1
    return s1[index - max_num: index], max_num

print(LSS('asdfgtr', 'asbnmcdfgt'))











'''
def dfs(start, k, n, sum1, res_cur):
    global count
    if sum1 > n or len(res_cur) > k:
        return

    elif sum1 == n and len(res_cur) == k:
        print(" ".join([str(x) for x in res_cur]))
        res.append(res_cur)
    else:
        for i in range(start, 10):
            res_cur.append(i)
            dfs(i + 1, k, n, sum1 + i, res_cur)
            res_cur.pop()


a = list(map(int, input().strip().split()))
k, n = a[0], a[1]
res = []
if n < 0 or n > 45:
    print("None")
else:
    dfs(1, k, n, 0, [])
'''



