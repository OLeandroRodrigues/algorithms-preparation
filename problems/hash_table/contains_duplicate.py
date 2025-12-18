"""
Problem: Contains Duplicate

Description:
Given an integer array `nums`, return True if any value appears at least twice
in the array, and return False if every element is distinct.

In other words, determine whether the array contains any duplicate elements.

Function Signature:
    def containsDuplicate(nums: List[int]) -> bool

Examples:
    Input: nums = [1, 2, 3, 1]
    Output: True

    Input: nums = [1, 2, 3, 4]
    Output: False

    Input: nums = [1, 1, 1, 3, 3, 4]
    Output: True

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Expected Approach:
    - Use a hash-based data structure (set or hash table)
    - Track previously seen elements
    - Return early as soon as a duplicate is detected

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

Notes:
    - The input array should not be modified.
    - Hash-based solutions are preferred over sorting for optimal performance.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        my_hashset = set()

        for element in nums:
            if element in my_hashset:
                return True
            my_hashset.add(element)
        
        return False
            