import random

def rand(n):
    return int(random.random() * n) + 1

def getKNumsRandom(k, max_num):
    if max_num < 1 or k < 1:
        return None
    res = [0] * k
    for i in range(k):
        res[i] = i + 1
    for i in range(k + 1, max_num):
        if rand(i) <= k:   #决定i进不进袋子
            res[rand(k) - 1] = i  #i随机替换掉袋子中的一个
    return res


print(getKNumsRandom(5, 100))


def rand(n):
    return int(random.random() * n) + 1



