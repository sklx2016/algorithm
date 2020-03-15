#方法一：遍历窗口，找出最大值

def maxWindows(array, size):
    length = len(array)
    end = size
    if length < size or size < 0:
        return []
    res = []
    while end <= length:
        res.append(max(array[end - size: end]))
        end += 1
    return res

print(maxWindows([1, 2, 3, 4, 5, 6, 5, 4 ,8 ,10], 3))

#方法二：定义双向队列，遍历数组，如果队列为空，存储这个数的下标，如果队列不为空， 而且队尾对应的数小于这个数， 则遍历队列， 每当队尾的数小于此数时， 删除队尾， 直到找到大于此数的数， 将此数放入队尾， 并检测队头是否超过滑动窗口其实位置
from collections import deque

def maxWindows2(array, size):
    length = len(array)
    if length < size or size < 0:
        return []
    res = []
    queueMax = deque([])
    queueMax.append(array[0])
    for x, y in enumerate(array[1 :], 1):
        if array[queueMax[-1]] <= y:
            for i in range(len(queueMax) - 1, -1, -1):
                if array[queueMax[i]] > y:
                    break
                else:
                    queueMax.pop()
        queueMax.append(x)
        if queueMax[0] <= x - size:
            queueMax.popleft()
        if x >= size - 1:
            res.append(array[queueMax[0]])
    return res

print(maxWindows2([1, 2, 3, 4, 5, 6, 5, 4 ,8 ,10], 3))


