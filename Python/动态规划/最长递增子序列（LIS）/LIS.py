def LIS(seq):
    m = len(seq)
    L = [1] * m
    for i in range(m):
        for j in range(i):
            if seq[j] < seq[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)


seq = [2, 3, 4, 1, 7]
print(LIS(seq))