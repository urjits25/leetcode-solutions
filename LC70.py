'''

CLIMBING STAIRS

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

'''
cache = {}
def climbStairs(n: int) -> int:
    if n < 3:
        return n
    if n in self.cache:
        return self.cache[n]
        
    ways = self.climbStairs(n-1) + self.climbStairs(n-2)
    self.cache[n] = ways
    return ways
