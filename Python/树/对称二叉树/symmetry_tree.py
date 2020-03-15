class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))



def symmetry_tree(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.value != right.value:
        return False
    return symmetry_tree(left.left, right.right) and symmetry_tree(left.right, right.left)

print(symmetry_tree(tree.left, tree.right))