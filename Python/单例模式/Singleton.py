#单例模式：一个类同一时间只有一个实例存在

# 使用__new__方法：
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
            return cls._instance




m = [(1, 2, 3), (1, 4, 6), (2, 1, 9)]
dict = {'Name': 6, 'Age': 7, 'Name2': 9 ,'Age2' : 8}
d = dict.setdefault('name3', 0)
for key, value in dict.items():
    print(key, value)
f = zip(dict.keys(), dict.values())
b = sorted(f, key = lambda x : x[1])
a = sorted(dict.items(), key = lambda x : x[1], reverse = True)
c = sorted(m, key = lambda x : x[1])
print(a)
print(b)
print(c)

'''

n, k = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
res1 = 0
sum_cur = 0
res_max = 0
length = len(A)
end = k
res2 = 0


if n == 0:
    print(0)
else:
    for i in range(n):
        if B[i] == 1:
            res1 += A[i]
        res2 += A[i]
    if k >= length:
        print(res2)
    else:
        while end < length:
            for j in range(k):
                if B[end - j] == 0:
                    sum_cur += A[end - j]
            res_max = max(res_max, sum_cur)
            sum_cur = 0
            end += 1
        print(res1 + res_max)

n = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
res = 0
count = 0
start = 0
end = 1
while start < n and end <= n:
    if max(A[start : end]) < min(B[start: end]):
        count += 1
        end += 1
        if end == n + 1:
            res += count * (count + 1) / 2
    else:

        res += count * (count + 1) / 2
        count = 0
        end += 1
        start = end - 1

print(res)
'''
