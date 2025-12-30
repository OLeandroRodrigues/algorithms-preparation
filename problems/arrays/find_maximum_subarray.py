"""
Maximum Subarray Problem (Kadane's Algorithm)

Problem:
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Example:
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach:
Kadane's Algorithm (Dynamic Programming)

At each position i:
    best_ending_here = max(nums[i], best_ending_here + nums[i])

We keep track of the global maximum seen so far.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Edge case: array with a single element
        if len(nums) == 1:
            return nums[0]

        # Initialize current_sum and max_sum
        current_sum = nums[0]
        max_sum = nums[0]

        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # Kadane's rule: extend previous subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global maximum if needed
            max_sum = max(max_sum, current_sum)

        return max_sum
