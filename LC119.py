'''

PASCAL'S TRIANGLE II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

'''

def getRow(k: int) -> List[int]:
    row = []
    for j in range(k+1):                                            # ---- kth row will have k elements
        row.append( self.getSum(k+1, j, k+1))
    return row

cached = {}                                                         # ---- Hash Map for memoization
def getSum(i: int, j: int, k: int) -> int:
    if (i,j) in self.cached:
        return self.cached[(i,j)]
    if j == 0:                                                      
        return 1
    if j == k-1:                                                    # ---- Elements at (k, 0) and (k, k)  = 1
        return 1
    sum = self.getSum(i-1, j, k-1) + self.getSum(i-1, j-1, k-1)
    self.cached[(i,j)] = sum
    return sum
