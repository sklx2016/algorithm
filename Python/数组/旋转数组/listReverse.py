A = [6, 7, 7 , 8, 9, 1, 2, 3, 4, 5]
def listReverse(array, target):
    start = 0
    end = len(array) - 1
    #mid = len(array) / 2
    while start < end:
        mid = int(start + (end - start) / 2)
        if target == array[mid]:
            return mid
        if array[mid] >= array[start]:
            if array[start] <= target and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if array[mid] < target and target <= array[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

print(listReverse(A, 8))

