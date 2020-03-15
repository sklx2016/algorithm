
#方法一：
def perm(array, start, end):
    global count
    if start == end:
        print(array)
        count += 1
    else:
        i = start
        for num in range(start, end):
            array[num], array[i] = array[i], array[num]
            perm(array, start + 1, end)
            array[num], array[i] = array[i], array[num]

count = 0
print(perm([1, 2, 3, 4], 0, 4))
print(count)



#方法二：
def perm2(array, res_cur, res):
    if len(res_cur) == len(array):
        print(res_cur)
        res.append(res_cur)
    else:
        for i in range(len(array)):
            if array[i] in res_cur:
                continue
            res_cur.append(array[i])
            perm2(array, res_cur, res)
            res_cur.pop()
res_cur = []
res = []
print(perm2([1, 2, 3, 4], res_cur, res))


#含有重复数字的全排列


def perm3(array, res_cur, res, used):
    if len(res_cur) == len(array):
        print(res_cur)
        res.append(res_cur)
    else:
        for i in range(len(array)):
            if used[i]:
                continue
            if i > 0 and array[i] == array[i - 1] and (not used[i - 1]):
                continue
            used[i] = 1
            res_cur.append(array[i])
            perm3(array, res_cur, res, used)
            used[i] = 0
            res_cur.pop()
array = [1, 2, 2, 3]
used = [0] * len(array)
res_cur = []
res = []
print(perm3(array, res_cur, res, used))






