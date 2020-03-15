def getLessIndex(array):
    if len(array) == 0:
        return -1
    length = len(array)
    if array[0] < array[1]:
        return array[0]
    if array[length - 1] < array[length - 2]:
        return array[length - 1]
    left  = 1
    right = length - 2
    while left < right:
        mid = (left + right) / 2
        if array[mid] > array[mid - 1]:
            right = mid - 1
        elif array[mid] > array[mid + 1]:
            left = mid + 1
        else:
            return array[mid]
    return array[left]