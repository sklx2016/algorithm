def strCal(string):
    num = []
    symbol = []
    index = 0
    s = ["+", "-", "*", "/"]
    neg = False
    while index < len(string):
        if string[index] not in s:
            cur = int(string[index])
            if neg:
                cur *= (-1)
                neg = False
            index += 1
            while index < len(string) and (string[index] == "*" or string[index] == "/"):
                if string[index] == "*" :
                    index += 1
                    cur *= int(string[index])
                    index += 1
                else:
                    index += 1
                    cur /= int(string[index])
                    index += 1
            if index == len(string):
                num.append(cur)
                break
            num.append(cur)
            symbol.append(string[index])
            index += 1
        else:
            neg = True
            index += 1

    res = num[0]
    num1 = num[1:]
    for i in range(len(num1)):
        if symbol[i] == "+":
            res += num1[i]
        else:
            res -= num1[i]
    print(int(res))

a = "-1+2-3*5+1*4/4+1"
strCal(a)









