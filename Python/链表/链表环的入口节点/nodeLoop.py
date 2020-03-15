class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def meetingNode(pHead):
    if not pHead:
        return None
    pSlow = pHead.next
    pFast = pSlow.next
    while pSlow != pFast:
        pSlow = pSlow.next
        pFast = pFast.next.next
    return pSlow

def nodeLoop(pHead):
    pFlag = meetingNode(pHead)
    if not pFlag:
        return None
    loopLength = 1
    meeting = pFlag
    while pFlag.next != meeting:
        pFlag = pFlag.next
        loopLength += 1
    pFast = pHead
    pSlow = pHead
    for i in range(loopLength):
        pFast = pFast.next
    while pFast != pSlow:
        pFast = pFast.next
        pSlow = pSlow.next
    return pFast.val

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
node6.next = node3


print(nodeLoop(node1))

