'''

LINKED LIST CYCLE II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

'''

# Two-pointer approach: O(1) space, in-depth explanation (https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783)
def detectCycle(head: ListNode) -> ListNode:
    '''
    :type head: ListNode
    :rtype: ListNode
    '''
    
    if not head or not head.next:
            return None

    slow, fast = head, head                                 
    while fast and fast.next:                               # ---- Tortoise and Hare Algorithm
        slow, fast = slow.next, fast.next.next

        if slow is fast:                                    # ---- Cycle found, iterate till we reach the start of the cycle
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow


# Hash-set solution - O(N) space
def detectCycle(head: ListNode) -> ListNode:
    '''
    :type head: ListNode
    :rtype: ListNode
    '''
        
    if not head:
            return None
   
    visited = set()                                         # ---- Hash set keeps track of visited ListNodes
    p = head

    while p and p not in visited:                           # ---- Loop breaks at the end of list, or beginning of cycle
        visited.add(p)
        p = p.next

    if not p:
        return None
    else:
        return p
