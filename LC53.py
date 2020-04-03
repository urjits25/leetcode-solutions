'''

MAXIMUM SUBARRAY

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

'''

# Dynamic Programming, Time : O(N); Space: O(N)
# Better solution (O(1) space): https://leetcode.com/problems/maximum-subarray/discuss/20194, Explanation: https://youtu.be/2MmGzdiKR9Y

def maxSubArray(nums: List[int]) -> int:
    sum_array = [nums[0]]
    
    for i in range(1, len(nums)):                                        
        sum_array.append(max(nums[i], nums[i] + sum_array[-1]) )        # ---- Start a new subarray OR Add new element to previous subarray
    return max(sum_array)                                               # ---- Maximum sum from corresponding subarrays 
