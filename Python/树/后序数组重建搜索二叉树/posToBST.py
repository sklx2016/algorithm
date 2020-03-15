class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

#判断一个数组是否为搜索二叉树的后序数组
def isPOST(array, start, end):
    if start == end:
        return True
    less = -1
    more = end
    for i in range(start, end):
        if array[end] > array[i]:
            less = i
        else:
            more = i if more == end else more

    if less == -1 or more == end:
        return isPOST(array, start, end - 1)
    if less != more - 1:
        return False

    return isPOST(array, start, less) and isPOST(array, more, end - 1)


print(isPOST([1, 2, 3, 4, 5], 0, 4))


#根据搜索二叉树的后序数组重建搜索二叉树
def posToBST(posArray, start, end):
    if start > end:
        return None
    head = Node(posArray[end])
    less = -1
    more = end
    for i in range(start, end):
        if posArray[end] > posArray[i]:
            less = -1
        else:
            more = i if more == end else more
    head.left = posToBST(posArray, start, less)
    head.right = posToBST(posArray, more, end -1)
    return head