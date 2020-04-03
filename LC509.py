'''

FIBONACCI NUMBER
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1.

Given N, calculate F(N).

'''

cache = {}                                                          # ---- Memoization to avoid duplicate computations
def fib(N: int) -> int:
    if N < 2:
        return N
    if N in self.cache:
        return self.cache[N]
    self.cache[N] = self.fib(N-1) + self.fib(N-2)
    return self.cache[N]
