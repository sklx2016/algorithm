def reOrderArray(array):
    j = len(array) - 1
    i = 0
    while i <= j:
        if array[i] % 2 != 0:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1
    return array

print(reOrderArray([1, 2, 3, 4, 5, 6, 7]))