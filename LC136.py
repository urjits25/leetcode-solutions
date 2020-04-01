'''

SINGLE NUMBER

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

def singleNumber(self, nums: List[int]) -> int:
    a = sum(nums)                                       # ---- 2N + X
    b = sum(set(nums))                                  # ---- N + X
    return b - (a - b)                                  # ---- (N + X) - (N)
