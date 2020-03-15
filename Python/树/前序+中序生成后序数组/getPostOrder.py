#思路：每当遍历到一个节点时（先序序列的第一个值），保存节点的值， 根据中序序列划分左子树和右子树，先遍历左子树， 后遍历右子树， 把节点的值放到后序序列中， 返回后序数组

class TreeNode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def getPostOrder(preOrder, inOrder, posOrder):
    if len(preOrder) == 1:
        posOrder.append(preOrder[0])
        return
    if len(preOrder) == 0:
        return
    root = posOrder[0]
    index = inOrder.index(posOrder[0])
    getPostOrder(preOrder[1 : index + 1], inOrder[:index], posOrder)
    getPostOrder(preOrder[index + 1 : ], inOrder[index + 1 : ], posOrder)
    posOrder.append(root)
    return posOrder



