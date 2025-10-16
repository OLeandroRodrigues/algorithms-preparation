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

import itertools
from typing import Any, List, Tuple, Set

class MinHeap:
    def __init__(self):
        self._data = []

    def insert(self, value: tuple) -> None:
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)

    def _heapify_up(self,i):
        while i > 0 and self._data[i] < self._data[(i - 1) // 2]:
            parent = (i - 1) // 2
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i = parent

    def _pop(self) -> tuple:
        if len(self._data) == 1:
            return self._data.pop()
        root = self._data[0]
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return root


    def _heapify_down(self,i) -> None:
        smallest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        if left < len(self._data) and self._data[left] < self._data[smallest]:
            smallest = left
        if right < len(self._data) and self._data[right] < self._data[smallest]:
            smallest = right
        
        if smallest != i:
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            self._heapify_down(smallest)


class PriorityQueue: 
    def __init__(self) -> None:
        self._heap = MinHeap()
        self._order = itertools.count()
    
    def push(self,value:Any, priority:int) -> None:
        order = next(self._order)
        self._heap.insert((priority,-order, value))
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('pop from an empty priority queue')
        
        priority, ng_order, value = self._heap._pop()
        return value
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('pop from an empty priority queue')
        
        priority, ng_order, value = self._heap._data[0]
        return value
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def __len__(self) -> int:
        return len(self._heap._data)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0 or k == 0:
            return []

        pq = PriorityQueue()
        visited: Set[Tuple[int, int]] = set()

        pq.push((0, 0), nums1[0] + nums2[0])
        visited.add((0, 0))

        ans: List[List[int]] = []
        while k > 0 and not pq.is_empty():
            i, j = pq.pop()
            ans.append([nums1[i], nums2[j]])

            # (i+1, j)
            if i + 1 < m and (i + 1, j) not in visited:
                pq.push((i + 1, j), nums1[i + 1] + nums2[j])
                visited.add((i + 1, j))

            # (i, j+1)
            if j + 1 < n and (i, j + 1) not in visited:
                pq.push((i, j + 1), nums1[i] + nums2[j + 1])
                visited.add((i, j + 1))

            k -= 1

            if len(ans) == m * n:
                break

        return ans