'''

SWAP NODES OF A LINKED LIST IN PAIRS 
Given a linked list, swap every two adjacent nodes and return its head. (In-place)

'''

# Time Complexity: O(N); Space Complexity: O(N) (Stack)
def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:                               # ---- Base condition, for empty or one node
        return head

    temp = head.next                                            # ---- Swap the pairs and return new head for subList
    head.next = temp.next
    temp.next = head
    head = temp

    head.next.next = self.swapPairs(head.next.next)             # ---- Recursively solve for further pairs
    return head
