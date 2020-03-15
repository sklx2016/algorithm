class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head, K):
    if(head == None or K < 2):
        return head
    temp = []
    index = head
    temp[0] = index
    for i in range(1, K):
        index = index.head
        if index != None:
            temp.append(index)
        else:
            return head
    temp[0].next = reverseKGroup(temp[K - 1].next, K)
    for i in range(1, K):
        temp[i].next = temp[i - 1]
    return temp[K - 1]



def twoPair(head):
    if head == None or head.next == None:
        return head
    left = head
    right = head.next
    left.next = twoPair(right.next)
    right.next = left
    return right

