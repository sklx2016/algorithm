class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def isBST(root, min1, max1):
    if root == None:
        return True
    if min1 != None and root.value < min1:
        return False
    if max1 != None and root.value > max1:
        return False
    return isBST(root.left, min1, root.value) and isBST(root.left, root.value, max1)
