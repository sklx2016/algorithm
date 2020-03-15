def uglyNumber(K):
    if K < 1:
        return 0
    res = [1]
    t2 = t3 = t5 = 0
    index = 1
    while index < K:
        minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
        res.append(minNum)
        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 3 <= minNum:
            t3 += 1
        while res[t5] * 5 <= minNum:
            t5 += 1
        index += 1
    return res[index - 1]

print(uglyNumber(10))


