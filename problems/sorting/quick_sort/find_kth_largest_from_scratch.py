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
##################### BEGIN NOTES ##########################################################################
##  The optimal solution for this problem would be based on the Quickselect algorithm.                    ##  
##  However, this type of approach has not yet been included in the theoretical section of the repository.##
##  Once it is covered, we will revisit this problem and include its optimal version.                     ##
##################### END   NOTES ##########################################################################
def quick_sort(arr, low, high):
        if low < high:
            q = partition(arr, low, high)
            quick_sort(arr, low, q - 1) # left side
            quick_sort(arr, q + 1, high) # right side
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def findKthLargest(A,k):
    if k < 1 or k > len(A):
        raise IndexError(f"k={k} is out of range for array of length {len(A)}")
    
    quick_sort(A, 0, len(A)- 1) 
    return A[-k]
     
# Sample of use
if __name__ == "__main__":
    A = [3,2,3,1,2,4,5,5,6]
    quick_sort(A, 0, len(A)- 1)
    print(A[-4])



        