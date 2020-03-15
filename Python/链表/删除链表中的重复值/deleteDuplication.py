class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplication(pHead):
    if not pHead:
        return None
    preHead = None
    pNode = pHead
    while pNode:
        nextNode = pNode.next
        needDelete = False
        if nextNode != None and pNode.val == nextNode.val:
            needDelete = True
        if not needDelete:
            preHead = pNode
            pNode = pNode.next
        else:
            pretoDelete = pNode
            nodeVal = pNode.val
            while pretoDelete.val == nodeVal and pretoDelete:
                pretoDelete = pretoDelete.next
            if preHead == None:
                pHead = pretoDelete
                pNode = pretoDelete
                continue
            else:
                preHead.next = pretoDelete
            pNode = pretoDelete
    return pHead