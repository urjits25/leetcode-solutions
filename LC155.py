'''

MIN STACK

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

Singly-Linked List implementation of Min Stack

'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy_min = ListNode(float(inf))
        self.dummy_stack = ListNode(float(inf))
        self.top_min = self.dummy_min
        self.top_s = self.dummy_stack
    
    def push(self, x: int) -> None:
        cur = ListNode(x)
        cur.next = self.top_s
        self.top_s = cur

        if self.top_s.val < self.top_min.val:
            cur = ListNode(x)        
        else:
            prev_min = self.top_min.val
            cur = ListNode(prev_min)
            
        cur.next = self.top_min
        self.top_min = cur
        
    def pop(self) -> None:
        
        if self.top_s is not self.dummy_stack:
            cur = self.top_s
            self.top_s = self.top_s.next
            del cur            

            cur = self.top_min
            self.top_min = self.top_min.next
            del cur

    def top(self) -> int:
        if self.top is not self.dummy_stack:
            return self.top_s.val

    def getMin(self) -> int:
        if self.top_min is not self.dummy_min:
            return self.top_min.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
