def FindNumberWithSum(array, sum):
    res = []
    i = 0
    j = len(array) - 1
    maxRes = 0
    while i < j:
        if array[i] + array[j] < sum:
            i += 1
        elif array[i] + array[j] > sum:
            j -= 1
        else:
            res = [array[i], array[j]]
            i += 1
            j -= 1
    return res

print(FindNumberWithSum([i for i in range(10)], 9))


dict = {'Name': 'Zara', 'Age': 7, 'Name2': 'Manni', 'Age2' : '8'}

for key, value in dict.items():
    print(key, value)