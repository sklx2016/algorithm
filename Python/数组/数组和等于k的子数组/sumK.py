test = [i for i in range(4)]

global res
res = []



def sumK(target, array, res_one, start):
    if target < 0:
        return
    elif target == 0:
        res.append(res_one)
    else:
        for i in range(start, len(array)):
            res_one.append(array[i])
            sumK(target - array[i], array, res_one, i)
            res_one.pop()


sumK(4, test, [], 0)
print(res)
