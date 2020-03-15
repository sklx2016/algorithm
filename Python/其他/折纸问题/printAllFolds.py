#产生第i + 1次折痕的过程，就是在对折i次产生的每一条折痕的两侧，依次插入上折痕和下折痕的过程
#
def printAllFolds(i, n, down):
    if i > n:
        return
    printAllFolds(i + 1, n, True)
    print("down" if down else "up")
    printAllFolds(i + 1, n, False)


printAllFolds(1, 3, True)