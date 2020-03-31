
        
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    '''
    :type headA: ListNode
    :type headB: ListNode
    :rtype: ListNode
    '''
    
    if not headA or not headB:
            return None
        
    pA = headA
    pB = headB

    while pA is not pB:
        pA, pB = pA.next, pB.next

        if not pA and not pB:                               # ---- End of both lists, no intersection
            return None

        if not pA:                                          # ---- Start from the other list
            pA = headB
        if not pB:                                          
            pB = headA
    return pA                                               # ---- Returns intersection node, after one traversal through lists
