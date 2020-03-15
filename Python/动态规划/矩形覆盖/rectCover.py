def rectCover(number):
    res = [0, 1, 2]
    for i in range(number - 2):
        res.append(res[-1] + res[-2])
    return res[number]

print(rectCover(5))






