'''
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder or  not inorder:
    	return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:len(left) + 1], left)
    root.right = buildTree(preorder[-len(right):], right)
    return root

