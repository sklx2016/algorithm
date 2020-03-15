class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def revererList(pHead):
    if not pHead or not pHead.next:
        return pHead
    else:
        last = None
        while(pHead):
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last

