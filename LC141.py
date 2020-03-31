'''

LINKED LIST CYCLE

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

'''

def hasCycle(head: ListNode) -> bool:

    '''
    :type head: ListNode
    :rtype: bool
    '''

    if not head or not head.next:                                   
            return False
        
        slow, fast = head, head.next                                     
        
        while slow and fast and fast.next and slow != fast:             # ---- Two pointers running at different speeds
            slow, fast = slow.next, fast.next.next
        
        if slow == fast:                                                # ---- Pointers eventually overlap if there's a cycle
            return True
        return False                                                    # ---- else reach the end of list
