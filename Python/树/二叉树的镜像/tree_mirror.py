class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


def treeMirror(root):
    if not root:
        return
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        treeMirror(root.left)
        treeMirror(root.right)

treeMirror(tree)