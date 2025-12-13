"""
Problem: Find Range of a Target Value Using Binary Search

Statement:
    Given a sorted array of integers and a target value,
    find the starting and ending index of the target in the array.
    If the target does not exist, return [-1, -1].

Constraints:
    - Array length n: 1 ≤ n ≤ 10⁴
    - Values range: -10⁴ < nums[i], target < 10⁴
    - The array is sorted in ascending order
    - The array may contain duplicate values

Goal:
    Compute the first and last positions where the target
    appears in the array using an efficient search strategy.

Approaches:
    - Version 1 (From Scratch):
        Use two modified binary searches:
        one to find the first occurrence (left boundary),
        and one to find the last occurrence (right boundary).

Complexity Targets:
    - Time: O(log n)
    - Space:
        - O(1) for iterative implementation
        - O(log n) for recursive implementation

How to run:
    pytest -q   # from the problems/ directory
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_left(nums, target), self.find_right(nums, target)]

    def find_left(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1      # keep searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def find_right(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1       # keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

