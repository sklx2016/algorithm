def nextGreatNumber(n):
    num = list(map(int, str(n)))
    i = len(num) - 2
    while i >= 0 and num[i + 1] <= num[i]:
        i -= 1
    if i == -1:
        return -1
    j = len(num) - 1
    while j >= 0 and num[j] <= num[i]:
        j -= 1
    num[i], num[j] = num[j], num[i]
    start = i + 1
    end = len(num) - 1
    while start < end:
        num[start], num[end] = num[end], num[start]
        start += 1
        end -= 1
    return str(num)



print(nextGreatNumber("154321"))
print(nextGreatNumber("54321"))



n = [1, 2]
print(''.join(map(str, n)))




