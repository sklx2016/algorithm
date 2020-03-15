def LinkNodeSort(head):
    tail = None
    cur = head
    smallPre = None
    small = None
    while cur != None:
        small = cur
        smallPre = Smallest(cur)
        if  smallPre != None:
            small = smallPre.next
            smallPre.next = small.next
        cur = cur if small != cur else cur.next
        if tail == None:
            head = small
        else:
            tail.next = small
        tail = small
    return head


def Smallest(head):
    smallPre = None
    small = head
    cur = head.next
    pre = head
    while cur != None:
        if cur.val < small.val:
            small = cur
            smallPre = pre
        pre = cur
        cur = cur.next
    return smallPre