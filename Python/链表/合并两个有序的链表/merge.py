class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(pHead1, pHead2):
    temp = ListNode(0)
    pHead = temp
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            temp.next = pHead1
            pHead1 = pHead1.next
        else:
            temp.next = pHead2
            pHead2 = pHead2.next
        temp = temp.next
    if pHead1:
        temp.next = pHead1
    if pHead2:
        temp.next = pHead2
    return pHead