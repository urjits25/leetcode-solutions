'''

REVERSE LINKED LIST II

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
 
'''

def reverseBetween(head: ListNode, m: int, n:int) -> ListNode:
    '''
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    '''
    
    # Function to reverse a subList
    # Returns the ListNode after the end of subList
    def reverseList(start: ListNode, end:ListNode) -> ListNode:
        l1 = start
        l2 = start.next
        while l1 != end:                                            # ---- Classic Link Reversal
            l3 = l2.next
            l2.next = l1
            l1, l2 = l2, l3
        return l2

    dummy = ListNode(0)                                             # ---- Dummy head to handle edge case
    dummy.next = head
    l1 = dummy

    start = head
    while m-1:                                                      # ---- Seek to start of subList
        if not m-2:                                                 # ---- (m-1)th ListNode
            l1 = start
        start, m, n = start.next, m-1, n-1

    end = start
    while n-1:                                                      # ---- Seek to end of subList
        end, n = end.next, n-1

    l2 = end.next                                                   # ---- (n+1)th node
    reverseList(start, end)                                         # ---- Reverse subList in-place

    if l1 == dummy:                                                 # ---- If subList starts from first ListNode, start from reversed
        head = end                                                  
    else:    
        l1.next = end                                               

    start.next = l2                                                 # ---- Last node from Reversed sublist points to (n+1)th node
    return head
