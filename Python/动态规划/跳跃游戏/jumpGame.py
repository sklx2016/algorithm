def jumpGame(array):
    if not array:
        return 0
    jump = 0
    cur = 0
    next = 0
    for i in range(len(array)):
        if cur < i:
            cur = next
            jump += 1
        next = max(next, array[i] + i)
    return jump




