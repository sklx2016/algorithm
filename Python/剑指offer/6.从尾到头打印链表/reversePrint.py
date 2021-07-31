'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reversePrint(head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
	stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack[::-1]
   



