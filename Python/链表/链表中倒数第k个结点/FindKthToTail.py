class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def FindKthToTail(K, pHead):
    p_First = pHead
    while K >= 0:
        p_First = p_First.next
        K -= 1
    while p_First:
        pHead = pHead.next
        p_First = p_First.next
    return pHead.next.val


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(FindKthToTail(2, node1))