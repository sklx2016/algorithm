def sortStack(stack):
    help = []
    while stack != []:
        cur = stack.pop()
        while help != [] and cur > help[-1]:
            stack.append(help.pop())
        help.append(cur)
    while help != []:
        stack.append(help.pop())
    return stack


a = [1, 3, 2, 4, 4, 2, 6]
print(sortStack(a))