'''
二叉树最大路径和，不一定过节点
'''

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

def max_path(root):
    global res
    if not root:
        return 0
    left = max_path(root.left)
    right = max_path(root.right)
    val = root.value
    if left > 0:
        val += left
    if right > 0:
        val += right
    res = max(res, val)
    return root.value + max(left, right)

global res
res = -100000

print(max_path(tree))
print(res)