'''

HAPPY NUMBER
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 

Those numbers for which this process ends in 1 are happy numbers.

'''

def helper(self, n:int) -> int:
    sq = 0        
    while n:
        sq += (n % 10) ** 2
        n //= 10
    return sq

# Calculate space complexity?, a better solution that saves space -> https://leetcode.com/problems/happy-number/discuss/56917/
def isHappy(self, n: int) -> bool:

    squares = set()                                             # ---- Seen squares of digits
    sq = self.helper(n)
    while sq != 1:

        if sq in squares:
            return False

        squares.add(sq)
        sq = self.helper(sq)

    return True 
