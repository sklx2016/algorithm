class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def help(root):
    def isBalance(node):
        if not node:
            return 0
        left = isBalance(node.left)
        right = isBalance(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return isBalance(root) != -1


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
print(help(tree))


a = [1, 2, 3]
print(id(a))
def f(x):
    b = x.append(2)
    print(x)
    print(id(x))
    print(id(b))

f(a)
