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


'''
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
'''
import sys

class Solution:

    res = -sys.maxsize
    def maxPathSum(self, root):
        return self.dfs(root)

    def dfs(self, node):
        if node == None:
            return 0
        left_max_sum = self.dfs(node.left)
        right_max_sum = self.dfs(node.right)
        sum_path = node.val
        sum_path = max(sum_path, sum_path + left_max_sum)
        sum_path = max(sum_path, sum_path + right_max_sum)
        self.res = max(self.res, sum_path)
        return max(0, left_max_sum, right_max_sum) + node.val


