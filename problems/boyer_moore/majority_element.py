"""
Problem: Majority Element

Description:
Given an integer array `nums`, return the element that appears more than
⌊ n / 2 ⌋ times, where n is the length of the array.

You may assume that the majority element always exists in the array.

Function Signature:
    def majorityElement(nums: List[int]) -> int

Examples:
    Input: nums = [3, 2, 3]
    Output: 3

    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Constraints:
    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

Expected Approach:
    - Use the Boyer–Moore Voting Algorithm for optimal performance
    - Alternatively, use a hash map to count frequencies

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1) using Boyer–Moore
    Space Complexity: O(n) using hash map

Notes:
    - The majority element is guaranteed to exist.
    - Sorting-based solutions are valid but less optimal (O(n log n)).
    - The Boyer–Moore algorithm is preferred in interview scenarios.
"""

from typing import List

class Solution:
    def majorityElement(nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

