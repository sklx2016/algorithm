def findContinueSequence(target):
    if target < 3:
        return []
    small = 1
    big = 2
    res = []
    mid = (target + 1) / 2
    cursum = small + big
    while small < mid:
        if cursum == target:
            res.append(list(range(small, big + 1)))
        while cursum > target and small < mid:
            cursum -= small
            small += 1
            if cursum == target :
                res.append(list(range(small, big + 1)))
                break
        big += 1
        cursum += big
    return res


print(findContinueSequence(50))


