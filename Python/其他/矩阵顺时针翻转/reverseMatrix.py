#矩阵翻转

def reverseMatrix(array):
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(i, col):
            array[i][j], array[j][i] = array[j][i], array[i][j]
    for i in range(col // 2):
        for j in range(row):
            array[j][i], array[j][col - 1 - i] = array[j][col - 1 - i], array[j][i]
    return array


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(reverseMatrix(a))




