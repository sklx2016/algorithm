from math import sqrt

#二分法
def sqrt_binary(num):
    x = sqrt(num)
    y = num / 2.0
    start = 0.0
    end = num * 1.0
    count = 1
    while abs(x - y) > 0.00000001:
        print(count, y)
        count += 1
        if y * y > num:
            end = y
            y = start + (end - start) / 2
        else:
            start = y
            y = start + (end - start) / 2
    return y


sqrt_binary(5)


#牛顿迭代法


def sqrt_newton(num):
    x = sqrt(num)
    y = num / 2.0
    count = 1
    while abs(x - y) > 0.00000001:
        print(count, y)
        count += 1
        y = ((y * 1.0) + (1.0 * num) / y) / 2
    return y


sqrt_newton(5)
