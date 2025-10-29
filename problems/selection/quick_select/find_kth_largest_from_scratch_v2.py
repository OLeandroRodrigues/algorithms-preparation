"""
Problem: 215. Kth Largest Element in an Array (leetcode)

Statement:
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5  

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    - 1 <= k <= nums.length <= 105
    - 104 <= nums[i] <= 104

Goal:
    Can you solve it without sorting?

Approaches:
    - Version 1 (From Scratch): implement required data structures manually.
    - Version 2 (Repo-based): reuse data_structures/ from this repo.

Complexity Targets:
    - Time: O (n log n)
    - Space: O (log n)

How to run:
    pytest -q  # from the problems/ directory
"""

import random

def quick_select(arr, low, high, k):
    if k < 1 or k > (high - low + 1):
        raise IndexError('k out of range')
    
    if low == high:
        return arr[low]

    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high],arr[pivot_index]
        
        p = partition(arr,low, high)

        rank = p - low + 1
        if rank == k:
            return arr[p]
        elif rank > k:
            return quick_select(arr, low, p -1, k)
        else:
            return quick_select(arr, p + 1, high, k - rank)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

