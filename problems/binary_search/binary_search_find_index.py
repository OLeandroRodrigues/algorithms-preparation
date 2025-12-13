"""
Note: Problem was got from Leetcode, link to the problem below:
https://leetcode.com/problems/binary-search/?envType=study-plan-v2&envId=binary-search

Problem: Binary Search in a Sorted Array 

Statement:
    Given a sorted array of integers and a target value,
    determine whether the target exists in the array and
    return its index if found, or -1 otherwise.

Constraints:
    - Array length n: 1 ≤ n ≤ 10⁴
    - Values range: -10⁴ < nums[i], target < 10⁴
    - All elements in the array are unique
    - The array is sorted in ascending order

Goal:
    Compute the index of the target value in the array using
    an efficient search algorithm, or return -1 if the target
    does not exist.

Approaches:
    - Version 1 (From Scratch):
        Implement the binary search algorithm manually using
        iterative or recursive logic.

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
    def search(self,nums: List[int], target:int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

