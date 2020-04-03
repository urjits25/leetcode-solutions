'''

REVERSE A LINKED LIST
Reverse a singly linked list.

'''

# Recursive Solution, Time Complexity: O(N) ; Space Complexity: O(N) (Stack)
def reverseList(head: ListNode) -> ListNode:
    return self.reverse(head, None)
        
def reverse(node: ListNode, prev: ListNode) -> ListNode:
    if not node: 
        return prev        
    n = node.next
    node.next = prev
    return self.reverse(n, node)
    

# Iterative Solution, Time complexity: O(N) ; Space Complexity: O(1)
def reverseList(head: ListNode) -> ListNode:
    if head and head.next:                                          # ---- For Linked Lists with two or more nodes
        i, j, k = head, head.next, head.next.next
        i.next = None
        while k:
            j.next = i
            i, j, k = j, k, k.next
        j.next = i
        head = j
    return head
