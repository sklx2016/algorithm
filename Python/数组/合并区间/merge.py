def section_merge(array):
    array = sorted(array, key = lambda x : x[0])
    print(array)
    res = []
    length = len(array)
    start = array[0][0]
    end = array[0][1]
    res_cur = []
    for i in range(1, length):
        if end > array[i][0]:
            end = max(end, array[i][1])
        else:
            res_cur.append(start)
            res_cur.append(end)
            res.append(res_cur)
            res_cur = []
            start = array[i][0]
            end = array[i][1]
    res.append([start, end])
    return res


a = [[1, 2], [2, 3], [5, 8], [1, 3], [6, 9], [100, 101]]
print(section_merge(a))















