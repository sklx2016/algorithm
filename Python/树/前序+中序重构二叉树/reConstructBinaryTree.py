class  TreeNode(object):
    def __init__(self,  value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def reConstructBinaryTree(preOrder , inOrder):
    if len(preOrder) == 0:
        return None
    if len(preOrder) == 1:
        return TreeNode(preOrder[0])
    else:
        node = TreeNode(preOrder[0])
        node.left = reConstructBinaryTree(preOrder[1: inOrder.index(preOrder[0] + 1)], inOrder[ : inOrder.index(preOrder[0])])
        node.right = reConstructBinaryTree(preOrder[inOrder.index(preOrder[0]) + 1 : ], inOrder[inOrder.index(preOrder[0]) + 1 : ])
        return node