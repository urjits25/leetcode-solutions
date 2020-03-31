'''

REMOVE NTH ELEMENT FROM END OF LIST

Given a linked list, remove the n-th node from the end of list and return its head.

Note: Given n will always be valid.

'''
    
def removeNthFromEnd(head: ListNodem n: int) -> ListNode:
    
    if not head:
            return head
            
    dummy = ListNode(0)
    dummy.next = head

    l2 = dummy
    while n:                                    # ---- Get N distance from start
        l2 = l2.next
        n -= 1

    l1 = dummy                                  # ---- Iterate till the last ListNode
    while l2.next:
        l1, l2 = l1.next, l2.next

    l1.next = l1.next.next                      # ---- Delete the nth from last end Node
    return dummy.next                           # ---- Return head / start ListNode
