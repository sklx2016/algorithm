#在数组中找出所有重复出现(2次)的数，要求时间复杂度O(n),空间复杂度O(1)

def findDouble(array):
    res = []
    for i in range(len(array)):
        if array[abs(array[i]) - 1] < 0:
            res.append(abs(array[i]))
        array[array[i] - 1] = -array[array[i] - 1]
    return res


print(findDouble([1, 1, 2, 3, 2, 4, 4, 5]))