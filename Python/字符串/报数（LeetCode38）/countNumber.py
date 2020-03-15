'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

'''

def countNumber(N):
    s = "1"
    count = 1
    res = ""
    for i in range(1, N):
        for j in range(len(s)):
            if j + 1 < len(s) and s[j] == s[j + 1]:
                count += 1
            else:
                res += str(count)
                res += s[j]
                count = 1
        s = res
        res = ""
    return s
print(countNumber(6))


