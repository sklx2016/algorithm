# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/1/10 16:35
=================================================='''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse (head : ListNode, tail: ListNode):
    prev = tail.next
    p = head
    while prev != tail:
        nex = p.next
        p.next = prev
        p = nex
        prev = p
    return tail, head

def reverseKGroup (head : ListNode, k : int):
    hair = ListNode(0)
    hair.next = head
    pre = hair
    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next
        nex = tail.next
        head, tail = reverseKGroup(head, tail)
        pre.next = head
        tail.next = nex
        pre = tail
        head = tail.next
    return hair.next
