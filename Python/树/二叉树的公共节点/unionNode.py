class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

#一般二叉树
def unionNode(node, node1, node2):
    if node == None or node == node1 or node == node2:
        return node
    else:
        left = unionNode(node.left)
        right = unionNode(node.right)
        if left and right:
            return node
        return left if left else right



#二叉搜索树
def findParent(node, node1, node2):
    if node1 == None or node2 == None:
        return
    if node1.val == node1.val:
        return
    val1 = node1.val
    val2 = node2.val
    while node != None:
        if (node.val - val1) * (node.val - val2) <= 0:
            return node.val
        elif node.val > val1 and node.val > val2:
            node = node.left
        else:
            node = node.right
    return False





