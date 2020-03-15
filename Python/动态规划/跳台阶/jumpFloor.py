
def jumpFloor(number):
    a = 1
    b = 1
    for i in range(number):
        a, b = b, a + b
    return a

def jumpFloor2(number):
    if number < 1:
        return 0
    elif number == 1:
        return 1
    else:
        return 2 * jumpFloor2(number - 1)


print(jumpFloor(10), jumpFloor2(5))

print(jumpFloor2(10))

#变态跳台阶

def jumpFloor(number):
    return 2**(number - 1)






'''

# 携程笔试  求信息增益

import math

def help(len_1, length):
    if len_1 == 0 or len_1 == length:
        return 0
    else:
        p_y_x = len_1 / (length * 1.0)
        return (p_y_x * math.log(p_y_x, 2) + (1.0 - p_y_x) * math.log((1.0 - p_y_x), 2)) * (length / (n * 1.0))

n = int(input())
count_1 = 0
dic = {}
for i in range(n):
    sample = list(map(int, input().strip().split(',')))
    if sample[1] == 1:
        count_1 += 1
    dic[sample[0]] = dic.setdefault(sample[0], []) + [sample[1]]

H_y = 0
p_y = count_1 / (n * 1.0)
if p_y == 1.0 or p_y == 0.0:
    H_y = 0.0
else:
    H_y = p_y * math.log(p_y, 2) + (1.0 - p_y) * math.log((1.0 - p_y), 2)

H_y_x = 0
for key, array in dic.items():
    count = 0
    for j in range(len(array)):
        if array[j] == 1:
            count += 1
    H_y_x += help(count, len(array))
print(round((H_y * (-1.0) + H_y_x), 2))
'''