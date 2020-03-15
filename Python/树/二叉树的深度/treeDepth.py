class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


def treeDepth(root):
    if not root:
        return 0
    left = treeDepth(root.left)
    right = treeDepth(root.right)
    return left + 1 if left >= right else right + 1




print(treeDepth(tree))