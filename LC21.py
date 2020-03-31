'''

MERGE TWO SORTED LISTS
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

@param l1, l2, ListNodes
@return head, a ListNode

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)                      # ---- Dummy head for merged list
        l3 = head
        
        while l1 and l2:                        # ---- Till we reach the end of at least one list
            if l2.val < l1.val:                 # ---- Compare the two ListNodes from L1 and L2
                l3.next = l2
                l2, l3 = l2.next, l3.next
            else:
                l3.next = l1 
                l1, l3 = l1.next, l3.next
        
        if l1:                                  # ---- Exhaust the remaining lists
            l3.next = l1
        if l2:
            l3.next = l2
        
        l3 = head.next
        del head                                # ---- Delete dummy head
        return l3
