#构建二叉树
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


#按层遍历
def levelOrder(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        nodes = []
        nodes_value = []
        for node in queue:
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            nodes_value.append(node.value)
        res.append(nodes_value)
        queue = nodes
    return res

#print(levelOrder(tree))


#深度遍历（中序 递归）
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)

#print(inOrder(tree))


#深度遍历 （前序 栈）
def preOrder(root):
    stack = []
    stack.append(root)
    while stack:
        head = stack.pop()
        print(head.value)
        if head.right:
            stack.append(head.right)
        if head.left:
            stack.append(head.left)

#preOrder(tree)


#(中序 栈)

def inOrder(root):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.value)
            root = root.right

inOrder(tree)




