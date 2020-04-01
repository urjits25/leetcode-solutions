'''

REMOVE LINKED LIST ELEMENTS

Remove all elements from a linked list of integers that have value val.

'''

def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        
        l1 = dummy
        while l1.next:                            
            if l1.next.val == val:                              # ---- Delete the node with given value
                l1.next = l1.next.next
            else: 
                l1 = l1.next
            
        return dummy.next                                       # ---- Return start of the List
