class Node(object):
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(4)), Node(2, Node(5), Node(5)))


def FindPath(root, expectNumber):
    if None == root: return []
    return FindAPath(root, expectNumber, [], [])

def FindAPath(root, expectNumber, path_list, lt):
    if None == root: return
    expectNumber = expectNumber - root.val
    lt.append(root.val)
    if expectNumber != 0:
        left_lt = list(lt)
        FindAPath(root.left, expectNumber, path_list, left_lt)
        right_lt = list(lt)
        FindAPath(root.right, expectNumber, path_list, right_lt)
    elif root.left == None and root.right == None:
        path_list.append(lt)
    return path_list

res = FindPath(tree, 8)
for i in range(len(res)):
    print(' '.join(map(str, res[i])))
