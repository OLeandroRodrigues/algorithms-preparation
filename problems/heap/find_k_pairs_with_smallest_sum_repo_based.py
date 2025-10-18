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

def find_k_pairs_with_smallest_sum_repo_based(
    nums1: List[int],
    nums2: List[int],
    k: int,
) -> List[Tuple[int, int]]:
    if k <= 0 or not nums1 or not nums2:
        return []

    n1, n2 = len(nums1), len(nums2)
    target = min(k, n1 * n2)

    # Repository's Min-PQ, interface: push(value, priority) and pop() -> value
    pq = PriorityQueue()

    # We limit the initially inserted "rows": at most k or n1
    # Each row i starts at j = 0
    limit_i = min(n1, k)
    for i in range(limit_i):
        u, v = nums1[i], nums2[0]
        sum = u + v
        # Lexicographic priority by values, stable by indices
        priority = (sum, u, v, i, 0)
        pq.push((i, 0), priority)   # value=(i,j)

    result: List[Tuple[int, int]] = []

    # k-way merge by rows (fixed i, advancing j)
    while len(result) < target and not pq.is_empty():
        i, j = pq.pop()            # pop() retorna o value (i, j)
        u, v = nums1[i], nums2[j]
        result.append((u, v))

        # Move forward in the same row (i), next j
        nj = j + 1
        if nj < n2:
            u2, v2 = nums1[i], nums2[nj]
            sum2 = u2 + v2
            priority2 = (sum2, u2, v2, i, nj)
            pq.push((i, nj), priority2)

    return result