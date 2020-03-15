class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#首尾相连构成环
def rotateListNode(head, k):
    if head == None:
        return head
    count = 1
    cur = head
    while cur:
        count += 1
        cur = cur.next
    if count % k == 0:
        return head
    k = k % count
    cur.next = head
    pre = head
    for _ in range(count - k):
        pre = pre.next
    cur = pre.next
    new_head = cur
    pre.next = None
    return new_head