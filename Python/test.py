#-*- coding:utf-8 -*-

'''

#alibaba 笔试
a = "我爱北京天安门"
b = "天安门"
print(a.index(b))
dic  = {"周杰": 1, "周杰伦": 2}
sorted_x=sorted(dic.items(),key= lambda x : x[0], reverse=True)
print(sorted_x)


singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听


list_1 = list(input().strip().split(';'))
dic = {}
for i in range(len(list_1)):
    list_i = list_1[i].strip().split('_')
    #print(list_i)
    shitiming = list_i[0]
    shitis = list_i[1].strip().split('|')
    for j in range(len(shitis)):
        dic[shitis[j]] = dic.setdefault(shitis[j], []) + [shitiming]

dic=sorted(dic.items(),key= lambda x : x[0], reverse=True)
dic = dict(dic)
#print(dic)
query = input()
query_list = []
res = ""
start = 0
index = -1
for i in range(len(query)):
    query_list.append(query[i])

for shiti, shitiming in dic.items():
    if shiti in query:
        #print(shiti)
        if query.index(shiti) != index:
            index = query.index(shiti)
            res += ''.join(query_list[start : index])
            res += " "
            start = index + len(shiti)
            res += shiti
            res += "/"
            for j in range(len(shitiming)):
                if j != len(shitiming) - 1:
                    res += shitiming[j]
                    res += ","
                else:
                    res += shitiming[j]
            res += " "

res += "".join(query_list[start : ])
print(res)




#2朋友圈
def dfs(array, i, visited):
    visited.add(i)
    for idx, val in enumerate(array[i]):
        if val == 1 and idx not in visited:
            dfs(array, idx, visited)

M = int(input())
array = []
for i in range(M):
    input_line = list(map(int, input().strip().split()))
    array.append(input_line)
if len(array) == 0:
    print(0)
else:
    visited = set()
    count, n = 0, len(array)
    for i in range(n):
        if i not in visited:
            dfs(array, i, visited)
            count += 1
    print(count)



#3  IP地址
def helper(s, dot_count, nums):
    global res
    if dot_count == 0 and len(s) == 0:
        res += 1
    elif len(s) > dot_count * 3 or len(s) < dot_count:
        return
    for i in range(3):
        if len(s) - 1 >= i:
            if (i == 2 and int(s[:i + 1]) > 255) or (i > 0 and s[0] == '0'):
                return
            nums.append(s[:i + 1])
            helper(s[i + 1:], dot_count - 1, nums)
            nums.pop()



#相似字符串
def judge(s, t):
    dic = {}
    for s1, t1 in zip(s, t):
        if s1 not in dic:
            dic[s1] = t1
        elif dic[s1] != t1:
            return False
    return len(set(dic.values())) == len(dic.values())

s = input()
t = input()
length = len(t)
start = 0
res = 0
while start + length <= len(s):
    sub_s = s[start : start + length]
    if judge(sub_s, t):
        res += 1
    start += 1
print(res)



class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_add:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

ListNode_1 = ListNode_add()
l1 = ListNode()
l1_list = list(map(int, input().strip().split()))
l1_list = l1_list[::-1]
k = int(input())
for i in l1_list:
    l1 = ListNode_1.add(i)


def reverseKGroup(head, k):
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return head
    prev = None
    curr = head
    for i in range(k):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    if curr:
        head.next = reverseKGroup(curr, k)
    return prev


res_head = reverseKGroup(l1, k)
res = []
while res_head:
    res.append(res_head.val)
    res_head = res_head.next

print(' '.join(map(str, res)))





def valid(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False

a = list(map(int, input().strip().split()))
res = 0
res_list = set()
for i in range(1, a[0] + 1):
    for j in range(1, a[1] + 1):
        for k in range(1, a[2] + 1):
            if str(sorted([i, j, k])) in res_list:
                res += 1
                continue
            elif valid(i, j, k):
                res_list.add(str(sorted([i, j, k])))
                res += 1
print(res % 1000000007)


a = [1, 2, 3]
b = [2, 1, 3]
c = set()
c.add(a)
c.add(b)
print(c)

def backtrack(index, res_cur, target, array):
    global res
    if target < 0:
        return
    if target == 0:
        res += 1
        return
    for i in range(index, len(array)):
        res_cur.append(array[i])
        backtrack(i, res_cur, target - array[i], array)
        res_cur.pop()


a = list(map(int, input().strip().split()))
N = a[0]
M = a[1]
b = list(map(int, input().strip().split()))
b = sorted(b)
print(b)
res = 0
d = []

backtrack(0, d, M, b)
print(res)




import math

def em(W, Y, y):
    emc = 0
    for i in range(len(Y)):
        if Y[i] != y[i]:
            emc += W[i]
    if emc == 0:
        return 1
    elif emc == 1:
        return 0
    else:
        return (math.log((1 - emc) / emc)) / 2.0


def refresh(W1, Y, y, am):
    zm = 0
    for i in range(len(Y)):
        zm += W1[i] * math.exp((-1) * am * Y[i] * y[i])
    for i in range(len(Y)):
        W1[i] = W1[i] * math.exp((-1) * am * Y[i] * y[i]) / (zm * 1.0)
    return W1


a = list(map(int, input().strip().split()))
Y = list(map(int, input().strip().split()))
M = a[0]
N = a[1]
K = a[2]
W = [1 / (N * 1.0)] * N
Am = []
for i in range(M):
    y = list(map(int, input().strip().split()))
    am = em(W, Y, y)
    Am.append(am)
    W = refresh(W, Y, y, am)

for i in range(K):
    t = list(map(int, input().strip().split()))
    res = 0
    for j in range(len(t)):
        res += Am[j] * t[j]
    #print(res)
    if res >= 0:
        print(1)
    else:
        print(-1)



class Node(object):
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right



tree = Node(1, Node(3, Node(7, Node(0)), Node(4)), Node(2, Node(5), Node(5)))


def FindPath(root, expectNumber):
    if None == root: return []
    return FindAPath(root, expectNumber, [], [])


def FindAPath(root, expectNumber, path_list, lt):
    if None == root: return
    expectNumber = expectNumber - root.val
    lt.append(root.val)
    if expectNumber != 0:
        left_lt = list(lt)
        FindAPath(root.left, expectNumber, path_list, left_lt)
        right_lt = list(lt)
        FindAPath(root.right, expectNumber, path_list, right_lt)
    elif root.left == None and root.right == None:
        path_list.append(lt)
    return path_list




res = FindPath(tree, 8)
for i in range(len(res)):
    print(' '.join(map(str, res[i])))

'''

'''
import random
def judge(array, res):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                res += 1
    return res


def count(array):
    res = 0
    index = 0
    for i in range(len(array)):
        cur = 0
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                cur += 1
        if cur > res:
            res = cur
            index = i
    return index


n = int(input())
A = list(map(int, input().strip().split()))
num = 0
idx = count(A)
A.insert(idx, 0)
A.pop(idx + 1)
print(str(judge(A, 0)) + " " + str(idx + 1))


'''
import collections

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

quot = collections.defaultdict(dict)

for (num, den), val in zip(equations, values):
    quot[num][num] = quot[den][den] = 1.0
    quot[num][den] = val
    quot[den][num] = 1 / val

for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]

[quot[num].get(den, -1.0) for num, den in queries]





def showTheSameChar(str1,str2):
    magic_chars = set(str1)
    len_str1 = len(magic_chars)
    poppings_chars = set(str2)
    len_str2 = len(poppings_chars)
    min_str = min(len_str1, len_str2)
    if min_str == 0:
        return True
    str = "".join(magic_chars & poppings_chars)
    len_str = len(str)
    if len_str * 1.0 / min_str > 0.9:
        return False
    else:
        return True

def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# filepath = "C:\\Users\\skkkkkk\\Desktop\\rude_result2.txt"
# filepath_write = "C:\\Users\\skkkkkk\\Desktop\\rude_result.txt"
# fpw=open(filepath_write, 'w', encoding='utf-8')
# fp=open(filepath, 'r', encoding='utf-8')
# content=fp.readlines()
# last = ""
# for c in content:
#     # str = c.split("\001")[0]
#     # cur = c.split("\001")[1]
#     cur = c
#     if str == '0':
#         continue
#     if showTheSameChar(cur, last):
#         fpw.write(cur)
#         print(cur)
#         last = cur
# fp.close()


# filepath = "C:\\Users\\skkkkkk\\Desktop\\rude_uniq.txt"
# filepath_write = "C:\\Users\\skkkkkk\\Desktop\\rude_result2.txt"
# fpw=open(filepath_write, 'w', encoding='utf-8')
# # fp=open(filepath, 'r')
# # content=fp.readlines()
# last = ""
# cnt = 0
# with open(filepath, 'r', encoding='utf-8') as fp:
#     content = fp.readlines()
#     for c in content:
#         cur = c.strip()
#         if is_contain_chinese(cur):
#             fpw.write(cur + '\n')
#             print(cnt)
#             cnt += 1
#
# fp.close()
# fpw.close()



# filepath = "C:\\Users\\skkkkkk\\Desktop\\rude.txt"
# filepath_write = "C:\\Users\\skkkkkk\\Desktop\\rude_result.txt"
# fpw=open(filepath_write, 'w', encoding='utf-8')
# # fp=open(filepath, 'r')
# # content=fp.readlines()
# last = ""
# cnt = 0
# with open(filepath, 'r', encoding='utf-8') as fp:
#     content = fp.readlines()
#     for c in content:
#         # str = c.split("\001")[0]
#         #     # cur = c.split("\001")[1]
#         cur = c.strip().split("\001")[1] + '\n'
#         fpw.write(cur)
#         print(cnt)
#         cnt += 1
#
# fp.close()
# fpw.close()
import json
import re
hits_list = []
# hit_dict = {
#       "workSet": [
#         {
#           "type": "text",
#           "text": {
#             "key1": "这是待标注的文本内容1"
#           }
#         }
#       ],
#       "metadata": {
#         "metadata1": "无"
#       }
#     }



# filepath = "C:\\Users\\skkkkkk\\Desktop\\all_result.txt"
# filepath_write = "C:\\Users\\skkkkkk\\Desktop\\all_result7.json"
# fpw=open(filepath_write, 'w', encoding='utf-8')
# fp=open(filepath, 'r', encoding='utf-8')
# content=fp.readlines()
# cnt = 1
# for c in content:
#     c = c.strip()
#     print(c)
#     hit_dict = {
#         "workSet": [
#             {
#                 "type": "text",
#                 "text": {
#                     "key1": "这是待标注的文本内容1"
#                 }
#             }
#         ],
#         "metadata": {
#             "metadata1": "无"
#         }
#     }
#     if cnt >= 60000 and cnt < 70000:
#         hit_dict["workSet"][0]["text"]["key1"] = c
#         hits_list.append(hit_dict)
#     cnt += 1
# dict_result = {"setName": "反垃圾", "hits" : hits_list}
# json_result = json.dumps(dict_result, indent=2, ensure_ascii=False)
# fpw.write(json_result)
# print(json_result)
# fp.close()


# filepath = "C:\\Users\\skkkkkk\\Desktop\\先放后审.json"
# filepath_write = "C:\\Users\\skkkkkk\\Desktop\\先审后放1.json"
# # old_dict = json.loads(filepath)
# # print(old_dict)
# fpw=open(filepath_write, 'w', encoding='utf-8')
# fp=open(filepath, 'r', encoding='utf-8')
# content=fp.readlines()
# cnt = 0
# for c in content:
#     c = c.strip()
#     hits= json.loads(c)["hits"]
#     print(hits[0])
#     for hit in hits:
#         text = hit["hit"]["workSet"][0]["text"]["text"]
#         hit_dict = {
#             "workSet": [
#                 {
#                     "type": "text",
#                     "text": {
#                         "key1": "这是待标注的文本内容1"
#                     }
#                 }
#             ],
#             "metadata": {
#                 "metadata1": "无"
#             }
#         }
#         hit_dict["workSet"][0]["text"]["key1"] = text
#         hits_list.append(hit_dict)
#         if c == 1000:
#             break
#         cnt += 1
#
# dict_result = {"setName": "反垃圾", "hits" : hits_list}
# json_result = json.dumps(dict_result, indent=2, ensure_ascii=False)
# fpw.write(json_result)
# print(json_result)
# fp.close()

# cnt = 6028
# str1 = ""
# for i in range(26):
#     str1 =  str1 +str(cnt)
#     str1 = str1 + ","
#     cnt += 1
# print(str1)
import random

def mapfunc(dic, list3):
    list2 = []
    list3.sort(reverse=True)
    print(list3)
    for i in list3:
        list2.append(dic[i])
    return list2

dict1 = {"12" : "normal", "40" : "erotic", "41" : "rude", "42" : "ads", "43" : "illegal", "44" : "others", "45" : "meaningless", "46" : "negative", "47" : "politics"}
filepath = "C:\\Users\\skkkkkk\\Desktop\\评论7.json"
filepath_write = "C:\\Users\\skkkkkk\\Desktop\\评论7_result.txt"
fpw=open(filepath_write, 'w', encoding='utf-8')
fp=open(filepath, 'r', encoding='utf-8')
content=fp.readlines()
cnt = 0
for c in content:
    c = c.strip()
    hits= json.loads(c)["hits"]
    #print(hits[0])
    for hit in hits:
        result = ""
        text = hit["hit"]["workSet"][0]["text"]["key1"]
        model = hit["result"]["labelAnswers"][0]["values"]
        print(model)
        model_real = "_".join(mapfunc(dict1, model))
        label = "bad"
        if model_real == "normal" :
            label = "good"
        dataset = "train"
        if random.random() > 0.8:
            dataset = "test"
        result = model_real + "\001" + text + "\001" + label + "\001" + dataset + "\n"
        fpw.write(result)
        # if cnt == 50:
        #     break
        cnt += 1
    print(cnt)
fp.close()
fpw.close()







































