"""
Problem: Two Sum

Statement:
    Given an array of integers and a target value,
    find two distinct indices such that the numbers at those
    indices add up to the target.

Constraints:
    - Array length n: 2 ≤ n ≤ 10⁴
    - Values range: -10⁹ < nums[i] < 10⁹
    - Target range: -10⁹ < target < 10⁹
    - Exactly one valid solution exists
    - The same element cannot be used twice

Goal:
    Compute the indices of the two numbers whose sum equals
    the target value.

Complexity Targets:
    - Time: O(n)
    - Space: O(n)

How to run:
    pytest -q   # from the problems/ directory
"""

from typing import List

class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:

        hash_table = {}
        for index, value in enumerate(nums):
            hash_table[value] = index

        for index, value in enumerate(nums):
            complement =  target - value
            if complement in hash_table and hash_table[complement] != index:
                return [hash_table[complement], index]
            
