#递归+回溯

class solution(object):
    def __init__(self, n):
        self.n = n

    def NQueens(self):
        if self.n < 1:
            return 0
        record = [0] * self.n
        return self.process(0, record)

    def process(self, i, record):
        if i == self.n:
            return 1
        res = 0
        for m in range(self.n):
            if self.valid(record, i, m):
                record[i] = m
                res += self.process(i + 1, record)
        return res

    def valid(self, record, i, m):
        for k in range(i):
            # 检验是否为同列 或者 同对角线（行-行 = 列-列）
            if record[k] == m or abs(i - k) == abs(m - record[k]):
                return False
        return True


def process(i, record, n):
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if valid(i, j, record):
            record[i] = j
            res += process(i + 1, record, n)
    return res

def valid(i, j, record):
    for k in range(i):
        if record[k] == j or abs(i - k) == abs(j - record[k]):
            return False
    return True




a = solution(4)
print(a.NQueens())





'''
def helper(dic, x, y):
    if x in dic.keys():
        list2 = [x]
        sum1 = int(dic[x][1])
        m = dic[x][0]
        count = 0
        while m in dic.keys():
            if m in list2:
                return 9
            if m == y:
                return 9
            list2.append(m)
            if count % 2 == 0:
                sum1 -= int(dic[m][1])
            else:
                sum1 += int(dic[m][1])
            count += 1
            m = dic[m][0]
            if m == y:
                return sum1
        return 9
    else:
        return 9

m, n = map(int, input().strip().split())
dic = {}
for i in range(m):
    list1 = input().strip().split()
    list_new = [list1[4], list1[2]]
    dic[list1[0]] = list_new

res = []
for j in range(n):
    list2 = input().strip().split()
    x, y = list2[0], list2[2]
    res_cur = helper(dic, x, y)
    res.append(res_cur)

for i in range(n):
    if res[i] == 9:
        print("cannot_answer")
    else:
        print(res[i])

'''


