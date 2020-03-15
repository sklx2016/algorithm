def moreThanHalf(array):
    count = 1
    number = array[0]
    for x in array[1:]:
        if x == number:
            count += 1
        else:
            count -= 1
            if count == 0:
                number = x
                count += 1
    sum = 0
    for x in array:
        if x == number:
           sum += 1
    return number if sum > len(array) // 2 else 0


print(moreThanHalf([4, 4, 1, 2, 3, 4, 4, 4,2, 5, 4, 4,1 ]))