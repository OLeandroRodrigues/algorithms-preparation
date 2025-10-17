"""
Problem: 373. Find K Pairs with Smallest Sums (leetcode)

Statement:
    You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
    Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Constraints:
    - 1 <= nums1.length, nums2.length <= 105
    - 109 <= nums1[i], nums2[i] <= 109
    - nums1 and nums2 both are sorted in non-decreasing order.
    - 1 <= k <= 104
    - k <= nums1.length * nums2.length

Goal:
    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Approaches:
    - Version 1 (From Scratch): implement required data structures manually.

Complexity Targets:
    - Time: ...
    - Space: ...

"""

from typing import List, Tuple
from python.data_structures.priority_queue.builtin.priority_queue_builtin import PriorityQueue

class Solution:
    def find_k_pairs_with_smallest_sum_repo_based(
        nums1: List[int],
        nums2: List[int],
        k: int,
    ) -> List[Tuple[int, int]]:
        if k <= 0 or not nums1 or not nums2:
            return []

        n1, n2 = len(nums1), len(nums2)
        limit_i = min(n1, k)

        # Min-priority queue by sum
        pq = PriorityQueue(is_min=True)

        # Store grid coordinates (i, j) as values; priority is the pair sum
        for i in range(limit_i):
            pq.push((i, 0), priority=nums1[i] + nums2[0])

        result: List[Tuple[int, int]] = []

        while not pq.is_empty() and len(result) < k:
            i, j = pq.pop()
            result.append((nums1[i], nums2[j]))
            if j + 1 < n2:
                pq.push((i, j + 1), priority=nums1[i] + nums2[j + 1])

        return result